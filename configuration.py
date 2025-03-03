"""
Configuration Module

This module contains configurations for the project, such as file paths,
email settings, and the URL to scrape.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Constants
FOLDER_PATH = "C:/PythonApp/"  # Path where the Excel file will be saved
FILE_NAME = "fibank_branches.xlsx"  # Name of the saved Excel file
SCRAPING_URL = "https://my.fibank.bg/EBank/public/offices"  # URL to scrape data

# Email Configuration
SENDER_EMAIL = "your_email@gmail.com"
RECIPIENT_EMAIL = "recipent_email@gmail.com"
EMAIL_SUBJECT = "Fibank Branches Data"
EMAIL_BODY = "Here is the Excel file with the Fibank branch information."

# Sensitive Information
EMAIL_PASSWORD = os.getenv("PASSWORD")
