import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Emailer:
    def __init__(self, sender_email, password, receiver_email):
        self.sender_email = sender_email
        self.password = password
        self.receiver_email = receiver_email

    def login_and_send(self):
        # Create message container and define emails
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "Data"
        msg["From"] = self.sender_email
        msg["To"] = self.receiver_email

        # Create the body of the email
        filename = "table.html"
        with open(filename, "r") as file:
            attachment = MIMEText(file.read(), "html")
            msg.attach(attachment)

        # Send the email
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login(self.sender_email, self.password)
        mail.sendmail(self.sender_email, self.receiver_email, msg.as_string())
        mail.quit()

