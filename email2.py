#kali ini kita akan menggunakan cara kedua

import smtplib
from email.message import EmailMessage

email_username = "laneigebankfile@gmail.com"
email_password = "laneigebankfile2013"

msg = EmailMessage()
msg["Subject"] = "selamat bergabung.."
msg["From"] = "Laneige Indonesia"
msg["To"] = "fadliselaz@gmail.com"
msg.set_content("selamat bergabung di komunitas kami..")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as mail:
    mail.login(email_username, email_password)
    mail.send_message(msg)
