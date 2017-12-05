# -*- coding: utf-8 -*-
from Fonctions import *

def mailTlm(mailTo, n_p):
    fromaddr = "numelopscra@gmail.com"
    toaddr = mailTo
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Liens discord"

    body = "Bonjour, " + n_p + "\n"
    body += "\nVoici le lien vers le discord Numelops : https://discord.gg/qMmYuB\n"
    body += "et en cadeau le lien vers le discord Imie général : https://discord.gg/9PaUBe.\n"
    body += "Si vous pouviez vérifier que tout le monde ait bien reçus le mail, viendez me voir sinon !\n"
    body += "\nThomas"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "FxNumelopsCrew")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


listN_P = ObtenirListN_P()
listMail = ObtenirListMail()

i=0
while i < len(listN_P):
    mailTlm(listMail[i], listN_P[i])
    i +=1