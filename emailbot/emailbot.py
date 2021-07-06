import smtplib
from email.message import EmailMessage
#creating server
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('infernoarju2000@gmail.com','Arjun@123')
email=EmailMessage()
email['From']='infernoarju2000@gmail.com'
email['To']='arjunpyromancer@gmail.com'
email['Subject']='Greeting message'
email.set_content('Hello paru happy xmas in advance')
server.send_message(email)