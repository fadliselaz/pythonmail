# kali ini kita akan coba untuk attach pdf file disini

import smtplib
from email.message import EmailMessage

us = "laneigebankfile@gmail.com"
ps = "laneigebankfile2013"

contact = ["fadliselaz@gmail.com", "bisri.h.kharisma@gmail.com", "ask.artace@gmail.com", "rompasregi5@gmail.com"]

msg = EmailMessage()
msg["Subject"] = "Penawaran Harga"
msg["From"] = "Fadli Selaz"
msg["To"] = ", ".join(contact)
msg.set_content("Dengan ini kami berikan penawaran harga\n pembuatan website..")

with open("test.pdf", "rb") as f:
    file_data = f.read()
    file_name = f.name

msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as mail:
    mail.login(us, ps)
    mail.send_message(msg)
    print("sent to : {}".format(msg["To"]))

