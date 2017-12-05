import datetime
import os

date = str(datetime.date.today()) +"_"

try:
    os.remove("D:\\IMIE\\Languages\\Python\\ScriptFx\\dateLundi.txt")
except:
    print("Fichier introuvable")

try:
    with open("D:\\IMIE\\Languages\\Python\\ScriptFx\\dateLundi.txt", "a") as fichier:
        fichier.write(date)
except:
    print("Erreur")