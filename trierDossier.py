# -*- coding: utf-8 -*-
import shutil
import os
from Fonctions import *
import datetime

#Vérifie si les fichiers dans le pathDrive ont bien l'extension .xls ou .xlsx
pathDrive = "C:\\Users\\thoma\\Google Drive\\IFTTT\\Gmail Attachments"
pathCRA = "D:\\IMIE\\Languages\\Python\\ScriptFx\\compteRendu\\CRA"
fichierDrive = os.listdir(pathDrive)
fichierCra = os.listdir(pathCRA)
extension = ["xlsx", ".xls", "XLSX", ".XLS"]


#Supprime si maj
i=0
while i < len(fichierDrive):
    for fichier in fichierCra:
        if fichierDrive[i] == fichier:
            os.remove(pathCRA + "\\" + fichier)
    i+=1

#Supprime l'extension du nom des fichiers
i = 0
while i < len(fichierDrive):
    if fichierDrive[i][-4:] in extension:
        print(fichierDrive[i])
        fichierDrive[i] = fichierDrive[i].replace(".xlsx", "")
        fichierDrive[i] = fichierDrive[i].replace(".XLSX", "")
        fichierDrive[i] = fichierDrive[i].replace(".xls", "")
        fichierDrive[i] = fichierDrive[i].replace(".XLS", "")
    else:
        os.remove(pathDrive + "\\" + fichierDrive[i])
    i+=1

#Recupere la liste Nom_Prenom de la BDD
listN_P = ObtenirListN_P()

#Verifie si les fichiers sont bien au format Nom_Prenom et si ça correspond à la liste de la BDD
i=0
while i < len(fichierDrive):
    if fichierDrive[i][:-4] not in listN_P:
        try:
            os.remove(pathDrive + "\\" + fichierDrive[i]+".xls")
        except:
            print("Erreur xls")
        try:
            os.remove(pathDrive + "\\" + fichierDrive[i] + ".xlsx")
        except:
            print("Erreur xlsx")
    i+=1


#Vérifie si les fichiers finnissent bien par le bon nom(selon le type de compte rendus) et les places dans les bon dossiers en fonction
types = ["CRA", "ODJ", "CRR"]
i = 0
while i < len(fichierDrive):
    if fichierDrive[i][-3:] in types:
        try:
            shutil.move(pathDrive+"\\"+fichierDrive[i]+".xls", "D:\\IMIE\\Languages\\Python\\ScriptFx\\compteRendu\\"+fichierDrive[i][-3:])
        except :
            print("Erreur")

        try:
            shutil.move(pathDrive + "\\" + fichierDrive[i] + ".xlsx", "D:\\IMIE\\Languages\\Python\\ScriptFx\\compteRendu\\" + fichierDrive[i][-3:])
        except:
            print("Erreur2")
    else:
        try:
            os.remove(pathDrive + "\\" + fichierDrive[i]+".xls")
        except:
            print("Erreur3")
        try:
            os.remove(pathDrive + "\\" + fichierDrive[i] + ".xlsx")
        except:
            print("Erreur4")
    i +=1

MajBadStudent()



