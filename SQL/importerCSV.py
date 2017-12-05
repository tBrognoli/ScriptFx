# -*- coding: utf-8 -*-
from Fonctions import *

listN_P = ObtenirListN_P()

listMail = ObtenirListMail()

listNom = list()
listPrenom = list()
listN_PSplit = list()
i=0
while i < len(listN_P):
    listN_PSplit = listN_P[i].split("_")
    listNom.append(listN_PSplit[0])
    listPrenom.append(listN_PSplit[1])
    i+=1

texte = "Nom;Prenom;Mail\n"
i=0
while i < len(listN_P):
    texte += listNom[i] + ";" + listPrenom[i] + ";" + listMail[i] +"\n"
    i +=1

with open("D:\\IMIE\\Languages\\Python\\ScriptFx\\SQL\\Membres.csv", "a") as FichierMembres:
    FichierMembres.write(texte)