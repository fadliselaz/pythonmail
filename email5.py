
# kali ini kita akan coba untuk masukan html file

import smtplib
from email.message import EmailMessage

us = "admin@artace.id"
ps = "fadliselaz13"

contact = ["fadliselaz@gmail.com", "bisri.h.kharisma@gmail.com",
           "ask.artace@gmail.com", "rompasregi5@gmail.com"]

msg = EmailMessage()
msg["Subject"] = "Penawaran Harga"
msg["From"] = "admin@artace.id"
msg["To"] = ", ".join(contact)
msg.set_content(
    "Dengan ini kami berikan penawaran harga\n pembuatan website..")

with open("test.pdf", "rb") as f:
    file_data = f.read()
    file_name = f.name

msg.add_alternative("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        body{
            min-height: 100vh;
            align-content: center;
        }
    </style>
</head>
<body>
    <center>
        <h1>Selamat datang di <br>komunitas kami</h1>
        <p>
            Berikut ini adalah link untuk validasi :<br> <br>
            <a href="http://artace.id">
                <button 
                style="border: 0ch; 
                width: 100px; 
                height: 30px;
                border-radius: 10px;
                background-color: blueviolet;
                color: white;
                ">Clik Disini</button>
            </a>
        
        </p>
    </center>
</body>
</html>

""", subtype="html")

with smtplib.SMTP_SSL("mail.artace.id", 465) as mail:
    print("coba masuk ...")
    mail.login(us, ps)
    print("Kirim pesan..")
    mail.send_message(msg)
    print("sent to : {}".format(msg["To"]))
