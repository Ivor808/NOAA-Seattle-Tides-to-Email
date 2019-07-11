import smtplib
import ssl


class Emailer:

    def __init__(self, email, password):
        self.port = 465
        self.email = email
        self.password = password

    def login_and_send(self):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', self.port, context=context) as server:
            server.login(self.email, self.password)