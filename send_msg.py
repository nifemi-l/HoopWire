import smtplib
from email.mime.text import MIMEText

# enter email and gmail app password *** (change email and enter app password)
EMAIL = "lawalwaryth@gmail.com"
PASSWORD = ""

# create send message function
def send_message(recipient, message, subject=""):
    """Send Message."""
    try: 
        # create MIMEText message with html type
        email_message = MIMEText(message, "html")
        
        # set email headers
        email_message["FROM"] = EMAIL
        email_message["To"] = recipient
        email_message["Subject"] = subject

        # store email address and password for easy access
        auth = (EMAIL, PASSWORD)

        # connect to gmail's smtp server
        # connect to 587 for TLS protocol
        server = smtplib.SMTP("smtp.gmail.com", 587)

        # initialize encryption
        server.starttls()

        # log into email account
        server.login(auth[0], auth[1])

        # send email to recipient  
        server.sendmail(auth[0], recipient, email_message.as_string())

        # close the connection
        server.quit()

    except Exception as e: 
        print(f'Error: {e}')