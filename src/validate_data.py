import pandas as pd

# Validate the data after cleaning to ensure it meets the required standards for analysis and follow-up email communication.

# Checks for: 
# - Valid email addresses
# - Valid phone numbers
# - Consistent age values
# - Properly formatted consent and survey status values

def validate_data(cleaned_patient_data: pd.DataFrame) -> pd.DataFrame:
    """
    Validate the cleaned patient data to ensure it meets the required standards.

    Args: patient_data (pd.DataFrame): The cleaned patient data to be validated.

    Returns: pd.DataFrame: The validated and invalidpatient data with any issues flagged.
    """
    validated_data = cleaned_patient_data.copy() # patient_data here is the cleaned version of the data. 


    # Validate impossible age (missing age, age less than 0, or age greater than 120)

    valid_age = validated_data["age"].between(0, 120)
    invalid_age = ~valid_age


    # Validate email addresses
    # previously, clean_data already cleaned up empty email values to empty string. 
    email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    valid_email = validated_data["email_address"].str.match(email_pattern, na=False) # check if the email address matches the pattern into boolean mask
    invalid_email = ~valid_email # filter out rows with invalid email address into boolean mask


    # Validate phone numbers (assuming valid phone numbers are 10 digits)
    # Cleaned up phone numbers are already in string format, so we can use regex to check for valid 10-digit phone numbers
    phone_pattern = r"^\d{10}$"
    
    valid_phone = validated_data["phone_number"].str.match(phone_pattern, na=False)
    invalid_phone = ~valid_phone # filter out rows with invalid phone number    


    # Validate consent values (should be boolean)
    valid_consent = validated_data["consent"].isin([True, False])
    invalid_consent = ~valid_consent


    # Validate survey status values (should be either 'completed' or 'incomplete')
    valid_survey_status = validated_data["survey_status"].isin(
    ["complete", "incomplete"])

    invalid_survey_status = ~valid_survey_status
    print("Total records:", len(validated_data))
    print("Valid age:", valid_age.sum())
    print("Valid email:", valid_email.sum())
    print("Valid phone:", valid_phone.sum())
    print("Valid consent:", valid_consent.sum())
    print("Valid survey status:", valid_survey_status.sum())

    valid_rows = (
        valid_age &
        valid_email &
        valid_phone &
        valid_consent &
        valid_survey_status
    )

    invalid_rows = (
        invalid_age |
        invalid_email |
        invalid_phone |
        invalid_consent |
        invalid_survey_status  
    )

    valid_data = validated_data[valid_rows] # filter out rows that are valid for all the checks
    invalid_data = validated_data[invalid_rows] # filter out rows that are invalid for any of the checks
    
    return valid_data, invalid_data