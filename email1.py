import smtplib
import os 
import time

class Sendmail:
    def __init__(self,us,ps,msg,frm,to):
        self.us = us
        self.ps = ps
        self.msg = msg
        self.frm = frm
        self.to = to

    def send(self):
        os.system("clear")
        try:
            
            print("connect to gmail...")
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            print("try to login..")
            mail.login(self.us, self.ps)
            subject = "Test Email From Python"
            body = self.msg
            content = f"Subject: {subject}\n\n{body}"
            
            mail.sendmail(self.frm, self.to, content)
            print(f"""
            ==========================================
            Berhasil Terkirim ke : {self.to}
            ==========================================
            """)


        except Exception as e:
            print("Error Bro.. \n", e)


username = "laneigebankfile@gmail.com"
password = "laneigebankfile2013"
kepada = input("\nmasukan alamat email pisahkan spasi : \n")
pesan = input("\nmasukan pesan : ")
dari = "Laneige Indonesia"

kirimEmail = Sendmail(username, password, pesan, dari, kepada)
kirimEmail.send()

