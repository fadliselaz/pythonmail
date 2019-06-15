#kali ini kita akan mencoba untuk attach image file..

import smtplib
import imghdr
from email.message import EmailMessage

username = "laneigebankfile@gmail.com"
password = "laneigebankfile2013"

#konsep pengiriman ini lebih terlihat professional
msg = EmailMessage()
msg["Subject"] = "please check this.."
msg["From"] = "LANEIGE Indonesia"
msg["To"] = "fadliselaz@gmail.com"

#ini adalah content managernya yang memunkinkan kita rapih dalam kirim email..
msg.set_content("This image attached please use as profile pict..!!")


with open("shutdown.jpg", "rb") as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name
msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)
    
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as mail:
    mail.login(username, password)
    mail.send_message(msg)
    print("file sent to : {}".format(msg["To"]))
