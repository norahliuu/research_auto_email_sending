# Create reminder email modeule to send followup emails to participants when their followup date is due. 

def generate_reminder_email(name: str) -> str:
    """
    Generate a reminder email for a participant.

    Args:
        name (str): The name of the participant.
    """
    subject = "Research Survey Reminder"
    email = f"""
    Dear {name},
    This is a friendly reminder to complete your follow-up survey. 
    Your participation is valuable to our research, 
    and we appreciate your time and effort.
    
    Thank you.
    """
    return subject,email 

import os 
import smtplib
from email.message import EmailMessage

def send_email(email_address: str, subject: str, email_body: str) -> None:

    """
    Send an email to the participant.

    Args:
        email_address (str): The email address of the participant.
        subject (str): The subject of the email.
        email_body (str): The body of the email.
    """
    sender_email = os.getenv('SENDER_EMAIL') # TODO: export email address and password in local terminal everytime before launch sending 
    sender_password = os.getenv('SENDER_PASSWORD')

    message = EmailMessage() # create an black email message object 

    message["From"] = sender_email 
    message["To"] = email_address
    message["Subject"] = subject
    
    message.set_content(email_body) 
    
    # Connect to Gamil server

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as email_server:
        email_server.login(sender_email, sender_password)
        email_server.send_message(message)