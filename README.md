# Clinical Research Data & Follow-Up Automation Engine

A Python-based clinical research data automation pipeline that cleans and validates participant data, stores validated records in a SQLite database, identifies participants requiring follow-up using SQL, and generates automated personalized email reminders.

This project was built to explore how Python and SQL can be used to reduce manual data processing and support reliable research data workflows.

> **Project Goal**: Helping automating the processing of data processing and emailing sending workflow in clinical research studies. 
> All participant data used in this project is synthetic. No real patient or clinical data is included.

## Features

- Imports synthetic participant data from CSV file 
- Cleans and standardizes participant information using pandas
- Validates values for:
  - Age
  - Email addresses
  - Phone numbers
  - Consent status
  - Survey completion status
- Separates valid and invalid records, store them in separate CSV fillers for future analysis 
- Generates a data quality report for invalid records
- Stores validated participants in a SQLite database
- Uses SQL queries to identify participants requiring follow-up
- Generates personalized survey reminder emails
- Supports automated email delivery through SMTP

## Skills and Technologies  

- **Python**: built the main data processing body and email processing pipeline with python
- **Pandas**: locate, clean, validate participant data using dataframe from pandas
- **SQL**: wrote queries to identify participants with needs to send follow up emails to
- **SQLite** — Built and maintained a participant database for validated research data
- **SMTP**: generate personalized reminder emails and auto-send to participants
- **REGEX**: validate and standardize email and phone number 

## Project Structure

    research_auto_email_sending_engine/
    |
    |-- data/
    |   |-- synthetic_participants_data.csv
    |
    |-- output/
    |   |-- data_quality_report.csv
    |   |-- validated_participants.csv
    |
    |-- src/
    |   |-- clean_data.py
    |   |-- validate_data.py
    |   |-- database.py
    |   |-- reminder_emails.py
    |
    |-- main.py
    |-- requirements.txt
    |-- README.md
    |-- .gitignore


## Data Processing

The pipeline first cleans raw participant data by standardizing fields such as phone numbers, consent values, survey status, and age.

The cleaned data is then validated against predefined data quality rules. Records that fail validation are separated and exported to a data quality report for review.

Only validated records are inserted into the SQLite participant database.

## Follow-Up Automation

SQL queries identify participants who:

- Have provided consent
- Have an incomplete survey
- Have reached their scheduled follow-up date

The system then generates a personalized reminder email for each eligible participant.

Email credentials are stored outside the source code using environment variables to avoid exposing sensitive authentication information.

## Running the Project

Install the required dependencies:

    pip install -r requirements.txt

Choose the email address used to send emails to participant for reminder
Set the required email environment variables:

    export SENDER_EMAIL="your_email@example.com"
    export SENDER_PASSWORD="your_app_password"

Run the pipeline:

    python main.py

## Privacy and Data Safety

This project is a demonstration using entirely synthetic participant data.

No real patient information, electronic health records, or personally identifiable clinical data are used or stored in this repository.
