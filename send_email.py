# send_email.py

import csv
import smtplib
from settings import SENDER_EMAIL, SENDER_PASSWORD, MENSAGEM_1, MENSAGEM_2


with open("csv_mails.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)


    smtp = smtplib.SMTP("smtp.meumail.com")
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(SENDER_EMAIL, SENDER_PASSWORD)


    for row in csv_reader:
        nome, email, coluna3, col4, col5 = row
        if coluna3 == "yes":
            msg = MENSAGEM_1.format(nome,col4)
            subject = "Título do Assunto"
        else:
            msg = MENSAGEM_2.format(nome)
            subject = "Outro Título"

        email_msg = "Subject: {} \n\n{}".format(subject,msg)
        smtp.sendmail(SENDER_EMAIL, email, email_msg)
        smtp.quit()
