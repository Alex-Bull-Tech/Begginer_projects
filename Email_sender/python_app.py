from email.message import EmailMessage
import ssl 
import smtplib

email_sender = 'alex.co.uk.official@gmail.com'
email_password = 'your own password'

email_receiver = 'target receiver email'

subject = "test"
body = """ 
When you watch a video, please follow along
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())  