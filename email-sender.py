import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    # Set up the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create a secure SSL connection
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Log in to the SMTP server
    server.login(sender_email, sender_password)

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    server.send_message(msg)

    # Quit the SMTP server
    server.quit()

# Example usage:
sender_email = 'abudu.m100302@st.futminna.edu.ng'
sender_password = 'Ab21du!?m'
recipient_email = 'auralex99@gmail.com'
subject = 'Test Email'
body = 'This is a test email sent from Python.'

send_email(sender_email, sender_password, recipient_email, subject, body)
