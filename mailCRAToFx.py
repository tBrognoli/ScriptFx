import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime

#Fonction supprime ancienne archive
def EraseFile(repertoire):
    files=os.listdir(repertoire)
    for i in range(0,len(files)):
        os.remove(repertoire+'\\'+files[i])

#Fonction zip le dossier
def zipperFichierCra(nom7zip):
    try:
        EraseFile("D:\IMIE\Languages\Python\ScriptFx\\archives")
    except:
        print("Fichier 7zp introuvable pour suppression")
    cmd = "7z a D:\\IMIE\\Languages\\Python\\ScriptFx\\archives\\" + nom7zip +" D:\\IMIE\\Languages\\Python\\ScriptFx\\compteRendu\\CRA\\*.*"
    
    os.system(cmd)

#Fonction mail pour fx
def mailToFx(myMail, mailTo, objectMail, text, zipName, pathZip, mdp ):
    fromaddr = myMail
    toaddr = mailTo

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = objectMail

    body = text

    msg.attach(MIMEText(body, 'plain'))

    filename = zipName
    attachment = open(pathZip + "\\" + zipName, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, mdp)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

def ObtenirDateLundi():
    try:
        with open("D:\\IMIE\\Languages\\Python\ScriptFx\\dateLundi.txt", "r") as fichier:
            dateLundi = fichier.read()
    except:
        print("Erreur")

    return dateLundi

def RenommerFichierCRA():
    fichierCRA = os.listdir("D:\\IMIE\\Languages\\Python\\ScriptFx\\compteRendu\\CRA")
    dateLundi = ObtenirDateLundi()
    i=0
    while i < len(fichierCRA):
        os.rename("D:\\IMIE\\Languages\\Python\\ScriptFx\\compteRendu\\CRA\\"+fichierCRA[i], "D:\\IMIE\\Languages\\Python\\ScriptFx\\compteRendu\\CRA\\"+dateLundi+fichierCRA[i])
        i+=1

################################################
date = str(datetime.date.today())


myMail = "numelopscra@gmail.com"
mailTo = "********@****.fr"
objectMail = "[NUMELOPS_ITLABS] Compte rendu "
text = "Bonjour FX, \nLes comptes rendus de la journée du "+date+" sont en pièce jointe. \nBonne soirée.\n\nCordialement,\nBROGNOLI Thomas"
zipName = "NUMELOPS_CRA_"+ date + ".7z"
pathZip = "D:\\IMIE\\Languages\\Python\\ScriptFx\\archives"
mdp = "**********"

RenommerFichierCRA()


#zipperFichierCra(zipName)
#RenommerFichierCRA()
mailToFx(myMail, mailTo, objectMail, text, zipName, pathZip, mdp )
EraseFile("D:\\IMIE\\Languages\\Python\\ScriptFx\\compteRendu\\CRA\\")
