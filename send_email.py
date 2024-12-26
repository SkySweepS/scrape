import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
from configuration import FILE_NAME, SENDER_EMAIL, RECIPIENT_EMAIL, EMAIL_SUBJECT, EMAIL_BODY, FOLDER_PATH, \
    EMAIL_PASSWORD

file_path = os.path.join(FOLDER_PATH, FILE_NAME)
smtp_server = 'smtp.gmail.com'
smtp_port = 587
password = EMAIL_PASSWORD
def send_email_with_attachment(sender_email=SENDER_EMAIL, receiver_email=RECIPIENT_EMAIL,
                               email_subject=EMAIL_SUBJECT, email_body=EMAIL_BODY):
    """
    Sends an email with an attachment (Excel file) to a specified recipient.

    This function constructs an email with a subject, body, and attachment,
    and sends it using Gmail's SMTP server. The attachment is loaded from
    the specified file path, which is formed by combining the folder path
    and file name.

    You can customize the email details (sender, recipient, subject, etc.)
    by modifying the corresponding values in the `configuration` module.

    The function uses the environment variable `PASSWORD` (loaded from a `.env` file)
    to log in to the Gmail account and send the email.

    Parameters:
        sender_email (str): The sender's email address. Edit variable 'from_email'
         in 'configuration' module in order to change the sender's email address.
        receiver_email (str): The recipient's email address. Edit variable 'to_email'
         in 'configuration' module in order to change the receiver's email address.
        email_subject (str): The subject of the email. Edit variable 'subject'
         in 'configuration' module in order to change the email's subject.
        email_body (str): The body of the email. Edit variable 'body'
         in 'configuration' module in order to change the email's body.

    Returns:
        None: This function does not return any value. It sends an email and prints the result.

    Raises:
        Exception: If the email cannot be sent due to issues with the SMTP server or login credentials.
    """
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = email_subject

    msg.attach(MIMEText(email_body, 'plain'))

    attachment = MIMEBase('application', 'octet-stream')
    with open(file_path, 'rb') as attachment_file:
        attachment.set_payload(attachment_file.read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', f'attachment; filename={FILE_NAME}')
    msg.attach(attachment)


    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

