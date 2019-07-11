import smtplib
import ssl


class Emailer:
    def __init__(self, sender_email, password, receiver_email, tide_data):
        self.port = 465
        self.sender_email = sender_email
        self.password = password
        self.receiver_email = receiver_email
        self.message = str(tide_data)

    def login_and_send(self):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=context) as server:
            server.login(self.sender_email, self.password)
            print(self.message)
            server.sendmail(self.sender_email, self.receiver_email, self.message)
