from send_email import send_email_with_attachment
from site_scrape import scrape_and_create



if __name__ == '__main__':
    scrape_and_create()
    send_email_with_attachment()