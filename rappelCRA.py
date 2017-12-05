# -*- coding: utf-8 -*-
import os
from Fonctions import *
import datetime

listN_P = ObtenirListN_P()
listMail = ObtenirListMail()

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
date = str(datetime.date.today())
badStudent = "      CRA manquant pour le " + date +"\n"


while i < len(listN_P):
    if listN_P[i] not in fichiersCRA:
        j += 1
        badStudent += str(j)+ "         " + listN_P[i] + "       " + listMail[i] + "\n"
        mailToNotSeriousStudent(listMail[i], listN_P[i], "CRA")
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
