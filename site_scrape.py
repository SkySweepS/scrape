import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd
import configuration


def scrape_and_create(folder_path=configuration.FOLDER_PATH,
                      file_name=configuration.FILE_NAME,
                      url=configuration.SCRAPING_URL):
    """
    Scrapes office information from a webpage and saves it as an Excel file.

    This function uses Selenium to scrape details about offices with extended working hours from a given URL.
    It extracts the office name, address, phone number, and working hours for Saturday and Sunday.
    The data is then saved as an Excel file in the specified folder path.

    Parameters:
        folder_path (str): The path to the folder where the Excel file should be saved.
         You can modify it in the `configuration` module as needed.
        file_name (str): The name of the Excel file to be saved.
         You can modify it in the `configuration` module as needed.
        url (str): The URL of the webpage to scrape.
         You can modify it in the `configuration` module as needed.
    Returns:
        None: This function does not return any value. It saves the scraped data into an Excel file.

    Notes:
        - The function uses a headless Chrome browser to scrape the webpage (no GUI).
        - The data is saved using the `openpyxl` engine in Excel format (.xlsx).
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        WebDriverWait(driver, 8).until(
            ec.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Удължено работно време')]"))
        )
        office_divs = driver.find_elements(By.XPATH, "//div[contains(text(), 'Удължено работно време')]")
        offices_data = []

        for office_div in office_divs:
            try:
                office_item = office_div.find_element(By.XPATH, "./ancestor::li")
                work_time = office_item.find_element(By.XPATH, ".//div[@sg-office-work-time]//dd//span").text
                work_time = work_time.split('.')

                if len(work_time) == 4:  # [0] = Monday-Friday, [1] = Saturday, [2] = Sunday, [3] = empty string
                    name = office_item.find_element(By.XPATH, ".//p[@bo-bind='item.name']").text
                    address = office_item.find_element(By.XPATH, ".//p[@bo-bind='item.address']").text
                    phone = office_item.find_element(By.XPATH, ".//p[@bo-bind='item.phones[0].phone']").text
                    work_time_saturday = work_time[1]
                    work_time_sunday = work_time[2]

                    offices_data.append({
                        'Офис': name,
                        'Адрес': address,
                        'Телефон': phone,
                        'Раб. време събота': f"{work_time_saturday}.",
                        'Раб. време неделя': f"{work_time_sunday}."
                    })
            except Exception as e:
                print(f"Error scraping an office: {e}")

        data = pd.DataFrame(offices_data)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_path = os.path.join(folder_path, file_name)
        data.to_excel(file_path, index=False, engine='openpyxl')
        print(f"File saved successfully to {file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
