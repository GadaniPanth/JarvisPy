import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from head.speak import speakBot


def email_send(to_whom, subject, content):
    sender_mail = "kingofkings082419@gmail.com"
    sender_pass = "cxvrkrfaosvhiqlx"
    receiver_mail = to_whom
    subject = subject
    message = content
    try:
        msg = MIMEMultipart()
        msg["From"] = sender_mail
        msg["To"] = receiver_mail
        msg["subject"] = subject
        msg.attach(MIMEText(message, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_mail, sender_pass)
            server.sendmail(sender_mail, receiver_mail, msg.as_string())
            speakBot(f"Done Sir!. Email Sent to {receiver_mail}.")
    except Exception as e:
        print(e)
