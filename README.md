# Fibank Branch Scraper and Email Sender

This project automates the process of scraping data about Fibank branches with extended working hours, storing the data in an Excel file, and sending the file via email.

## Features

- **Web Scraping**: Scrape Fibank branch details, including name, address, phone number, and weekend working hours.
- **Excel Generation**: Save scraped data in an organized Excel file format.
- **Email Automation**: Send the Excel file as an email attachment automatically.
- **Secure Configuration**: Handles sensitive information (e.g., email credentials) securely using environment variables.

---

## Project Structure

```plaintext
├── main.py            # Main script triggering the scraping and email sending process
├── configuration.py   # Handles configurable parameters and email settings
├── site_scrape.py     # Performs web scraping and Excel file generation
├── send_email.py      # Sends the generated Excel file via email
├── .env               # Stores sensitive environment variables securely (e.g., email password)
```

---

## Prerequisites

Before running this project, ensure that you have installed the required dependencies and set up the environment:

1. **Python Version**: Python 3.8 or higher
2. **Google Chrome**: Installed on your machine (required for Selenium)
3. **ChromeDriver**: Installed to control Chrome (ensure it matches your Chrome version)
4. **Python Libraries**:
    - selenium
    - pandas
    - openpyxl
    - python-dotenv
5. **Environment File**: Create a `.env` file in the root directory for secure storage of sensitive data.

Install the required Python libraries using:
```bash
pip install selenium pandas openpyxl python-dotenv
```

---

## Configuration

1. **Environment Variables**:
   Place sensitive credentials (e.g., email password) in the `.env` file to avoid hardcoding. Example:
   ```plaintext
   PASSWORD=your_email_password
   ```

2. **Adjust Configuration in `configuration.py`**:
    - Folder Path: Path to save the generated Excel file (`FOLDER_PATH`)
    - File Name: Name for the generated file (`FILE_NAME`)
    - Scraping URL: URL to scrape data (`SCRAPING_URL`)
    - Email settings:
        - Sender email: (`SENDER_EMAIL`)
        - Recipient email: (`RECIPIENT_EMAIL`)
        - Email Subject and Body: (`EMAIL_SUBJECT` and `EMAIL_BODY`)

---

## How to Run

1. **Run the Main Script**:
   The entire workflow (scraping + email-sending) is executed from `main.py`. Run the following command in the terminal:
   ```bash
   python main.py
   ```

2. **Scrape Data**:
   The `scrape_and_create` function in `site_scrape.py` will scrape Fibank branches' information and save it as an Excel file in the specified folder path (`FOLDER_PATH`).

3. **Send Email**:
   The `send_email_with_attachment` function in `send_email.py` sends the generated Excel file to the specified recipient (`RECIPIENT_EMAIL`).

4. **Output**:
    - Scraped data will be saved as an Excel file, e.g.:
      ```plaintext
      C:/PythonApp/fibank_branches.xlsx
      ```
    - A confirmation message is printed if the email is sent successfully.

---

## Example Usage

1. **Excel File**:
   The scraped information includes the following columns:
    - Офис (Branch Name)
    - Адрес (Address)
    - Телефон (Phone Number)
    - Раб. време събота (Working Hours Saturday)
    - Раб. време неделя (Working Hours Sunday)

2. **Email**:
   The generated Excel file is sent to the recipient as per the configured details (`RECIPIENT_EMAIL`).

---

## Error Handling

- **Web Scraping**:
    - If some data cannot be scraped, the program skips that entry and logs the issue.
    - Ensure the page structure matches the expected XPath queries in the `site_scrape.py` file.

- **Email Sending**:
    - Ensure your `.env` file includes the correct email password for `SENDER_EMAIL`.
    - Make sure Gmail allows "less secure apps" or use an App Password for stricter security.

- **Driver Issues**:
    - Ensure you have the correct `chromedriver` version installed that matches your Chrome browser version.

---

## License

This project is licensed under the **MIT License**. Feel free to modify it according to your needs.