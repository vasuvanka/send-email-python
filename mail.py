import smtplib


class Email(object):
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.smtp_server = None

    def connect(self):
        self.smtp_server = smtplib.SMTP(host=self.host, port=self.port)
        self.smtp_server.starttls()
        self.smtp_server.login(self.username, self.password)
        print("connected")

    def send(self, to, text):
        print("sending email")
        return self.smtp_server.sendmail(
            from_addr=self.username, to_addrs=to, msg=text)

    def disconnect(self):
        self.smtp_server.quit()
        print("disconnected")
