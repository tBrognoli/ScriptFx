# -*- coding: utf-8 -*-
import pymysql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


class Membres:
    def __init__(self, nom, prenom,gMail):
        self.nom = nom
        self.prenom = prenom
        self.gMail = gMail

#Connecte la BDD et crée une liste de Membres
db = pymysql.connect("localhost", "root", "", "numelops")
cursor = db.cursor()
sql = "SELECT * FROM membres"
listMembres = list()
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        listMembres.append(Membres(row[1], row[2], row[3]))
except:
    print("Error")
db.close()


#Retourne une liste au format Nom_Prenom par rapport à la BDD
def ObtenirListN_P():
    listN_P = list()
    for Membres in listMembres:
        listN_P.append(str(Membres.nom + "_" + Membres.prenom))
    return listN_P

#Envois MailType aux personnes n'ayant pas envoyé le compte rendu
def mailToNotSeriousStudent(mailTo, n_p, type):
    fromaddr = "numelopscra@gmail.com"
    toaddr = mailTo
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Rappel envois " + type

    body = "Bonjour, " + n_p + "\n"
    body += "\nMerci de bien vouloir m'envoyer votre CRA avant vendredi 16h30.\n"
    body += "Bonne soirée !\n"
    body += "\nNumelops' Bot"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "FxNumelopsCrew")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

#Retire l'extension au nom du fichier
def RetirerExtension(fichiersCRR):
    extension = ["xlsx", ".xls", "XLSX", ".XLS"]
    i = 0
    while i < len(fichiersCRR):
        if fichiersCRR[i][-4:] in extension:
            fichiersCRR[i] = fichiersCRR[i].replace(".xlsx", "")
            fichiersCRR[i] = fichiersCRR[i].replace(".XLSX", "")
            fichiersCRR[i] = fichiersCRR[i].replace(".xls", "")
            fichiersCRR[i] = fichiersCRR[i].replace(".XLS", "")
        i+=1
    return fichiersCRR

#Retire '_CRR' au nom du fichier
def RetirerType(fichiersCRR, type, listN_P):
    i=0
    while i < len(fichiersCRR):
        if fichiersCRR[i][:-4] in listN_P:
            fichiersCRR[i] = fichiersCRR[i].replace(type, "")
        i+=1
    return fichiersCRR

#Retourne la liste des adresses mail de chaque Membres
def ObtenirListMail():
    listMail = list()
    for Membres in listMembres:
        listMail.append(Membres.gMail)
    return listMail

#Récupere la date du lundi depuis un fichier txt
def ObtenirDateLundi():
    try:
        with open("D:\\IMIE\\Languages\\Python\ScriptFx\\dateLundi.txt", "r") as fichier:
            dateLundi = fichier.read()
    except:
        print("Erreur")

    return dateLundi


#Met à jour le fichier badStudent
def MajBadStudent():
    listN_P = ObtenirListN_P()

    pathCRA = "D:\\IMIE\\Languages\\Python\\ScriptFx\\compteRendu\\CRA"
    fichiersCRA = os.listdir(pathCRA)

    #Retire l'extension au nom du fichier
    fichiersCRA = RetirerExtension(fichiersCRA)

    #Retire '_CRA' au nom du fichier
    fichiersCRA = RetirerType(fichiersCRA, "_CRA", listN_P)

    #Verifie si le fichier est déjà présent et envois un mail de rappel si il ne l'est pas
    dateLundi =  ObtenirDateLundi()
    i = 0
    j= 0
    badStudent = "      CRA manquant pour semaine lundi " + dateLundi +"\n"


    while i < len(listN_P):
        if listN_P[i] not in fichiersCRA:
            j += 1
            badStudent += str(j)+ "         " + listN_P[i] +"\n"
        i +=1
    try:
        os.remove("C:\\Users\\thoma\\Google Drive\\IFTTT\\BadStudents" + dateLundi + ".txt")
    except:
        print("Fichier introuvable")

    try:
        with open("C:\\Users\\thoma\\Google Drive\\IFTTT\\BadStudents" + dateLundi + ".txt", "a") as fichier:
            fichier.write(badStudent)
    except:
        print("Erreurtxt")
