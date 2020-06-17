# send mail
import smtplib
import mail
port = 587
host = "smtp-mail.outlook.com"
password = "password"
username = "user email"
to_list = ["vanka.vasu@gmail.com"]
message = """From: from email <from@email.in>
To: Vasu Vanka <vanka.vasu@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

mailer = mail.Email(host=host, port=port, username=username, password=password)

mailer.connect()
mailer.send(to=to_list, text=message)
mailer.disconnect()
