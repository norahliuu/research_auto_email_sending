# Clean up messy patients data and prepare it for analysis and followup email sending

# Synthetic patient data always has patient id for each row; Name, age, survey status and followup_date are automatically recoreded by the form.
# Email, phone number may be missing since they are collected from the participants. 

import pandas as pd

def clean_data(patient_data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and standardize the patient data. 

    Standardizes consent and survey status values, handles missing
    email and phone information, and converts age values to numeric
    format.

    Args: patient_data (pd.DataFrame): The raw patient data to be cleaned.
    Returns: pd.DataFrame: The cleaned and standardized patient data. 
    """
    # Copy the original data to avoid modifying it directly

    cleaned_data = patient_data.copy()

    #clean up "age" column by converting it to numeric and handling missing values

    cleaned_data["age"] = pd.to_numeric(
        cleaned_data["age"], errors="coerce" # turn in NaN when the value cannot be converted to numeric
    )
    
    # cleam up "email" column 
    cleaned_data["email_address"] = (
        cleaned_data["email_address"]
        .fillna("") #fill missing email values with empty string
        .str.strip()
        .str.lower()
    )

    # clean up "phone_number" column by removing any non-numeric characters and standardizing the format to strings 
    cleaned_data["phone_number"] = (
        cleaned_data["phone_number"]
        .fillna("") # fill missing phone number values with empty string
        .astype(str)
        .str.strip()
        .str.replace(r"\.0$", "", regex=True) #remove trailing ".0" from phone numbers that may have been converted to float by pandas
        .str.replace(r"\D", "", regex=True) # remove any non-numeric characters from phone numbers like "-", "(", ")", " ", etc.
    )

    # clean up the 'consent' column by standardizing the yes/novalues to boolean 
    cleaned_data["consent"] = (
        cleaned_data["consent"]
        .astype(str)
        .str.strip()
        .str.lower()
        .replace({"yes": True, "no": False, "y": True, "n": False})
    )

    # cleam up "survey_status" column by standardizing the values to a consistent format
    cleaned_data["survey_status"] = (
        cleaned_data["survey_status"]
        .str.strip()
        .str.lower()
        .replace({"completed": "completed", "incomplete": "incomplete"})    
        
    )
    
    return cleaned_data 



