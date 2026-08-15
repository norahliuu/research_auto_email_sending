# Data cleaning pipeline for the project 
# Take patients data and clean it for analysis and purpose of sending followup email

import pandas as pd
from src.clean_data import clean_data
from src.validate_data import validate_data 
from src.database import create_connection

# Read the synthetic patient data from the CSV file 
patient_data = pd.read_csv('data/synthetic_participants_data.csv')

# Clean the patient data using the function from clean_data.py 
cleaned_data = clean_data(patient_data) # cleaned_data is the cleaned version of the data.
print(cleaned_data) 

# Validate the cleaned pateint data using the function from validate_data.py
# Get the valid and invalid datadrame 
valid_data, invalid_data = validate_data(cleaned_data)

# output the invalid data to a csv file for data quality report. 
invalid_data.to_csv(
    "output/data_quality_report.csv",
    index=False
)

# output the valid data to a csv file for furture analysis. 
valid_data.to_csv(
    "output/validated_participants.csv",
    index=False
)
print(cleaned_data["phone_number"].head(10))

print(len(valid_data), "valid records saved to output/validated_participants.csv")
print(len(invalid_data), "invalid records saved to output/data_quality_report.csv")

# Initalize the database connection and create table named participants in the .db if it does not exist.
connection = create_connection()

print("Database connected successfully.")

# Insert validated into the database table named participants. 
from src.database import (insert_data, get_followup_participants)

insert_data(connection, valid_data) # insert the validated data into the database table named participants.
needed_followup_participants = get_followup_participants(connection) # Get the participants who need followup based on the required criteria (e.g., consented participants with incomplete surveys).

connection.close() # close the database connection after inserting the data and getting the followup participants.


# Send out reminder emails to participants need followup with by using functions from src.reminder_emails
from src.reminder_emails import (generate_reminder_email, send_email)

for participant in needed_followup_participants:
    name = participant[1].capitalize()
    email = participant[2]

    subject, email_body = generate_reminder_email(name)
    send_email(email, subject, email_body)


    