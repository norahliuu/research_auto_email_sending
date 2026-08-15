import sqlite3
import pandas as pd

# Create a connection to the research participant database and create the participants table if it doesn't exist.
def create_connection(): 
    """
    Create a connection to the research participant database.

    Returns:
        A connection to the SQLite database.
    """

    connection = sqlite3.connect("data/research.db") # set up connection to the database  
                                                     # connect to research.db  
    connection.execute("""
    CREATE TABLE IF NOT EXISTS participants (
        patient_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        email_address TEXT,
        phone_number TEXT,
        consent BOOLEAN,
        survey_status TEXT,
        followup_date TEXT)
    """)    

    connection.commit()

    return connection


# Insert validated participant data into the database table created above.
def insert_data(connection, valid_data: pd.DataFrame):
    """
    Insert validated participant data into the database table.

    Args:
        connection: The SQLite database connection.
        valid_data (pd.DataFrame): The validated participant data to be inserted.
    """

    for index, participant in valid_data.iterrows(): # iterate through each row in validated dataframe  
        connection.execute("""
        INSERT OR REPLACE INTO participants 
        (patient_id, name, age, email_address, phone_number, consent, survey_status, followup_date) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, # insert each column value to the database table named participants using sql commands 
        (
            participant["patient_id"], # insert each column value into the database table
            participant["name"],
            participant["age"],
            participant["email_address"],
            participant["phone_number"],
            participant["consent"],
            participant["survey_status"],
            participant["followup_date"]
        )) 
    connection.commit()

# Select participant data from the database table which needs followup based on the required critiria (e.g., consented participants with incomplete surveys).
def get_followup_participants(connection):
    """
    Get participants from the database who need follow-up based on specific criteria.
    """

    # Select participants who have consented by SQL query  
    cursor = connection.execute("""
    SELECT patient_id, name, email_address, followup_date
    FROM participants
    WHERE consent = 1 AND survey_status = 'incomplete' AND followup_date <= date('now')
    """) # select all columns from the database table named participants where consent is True and survey_status is incomplete

    return cursor.fetchall() # return the selected rows from the database table as a list of tuples