import pymysql

class Membres:
    def __init__(self, nom, prenom, eMail, gMail):
        self.nom = nom
        self.prenom = prenom
        self.eMail = eMail
        self.gMail = gMail


db = pymysql.connect("localhost", "root", "", "numelops")

cursor = db.cursor()

with open('listMembres.csv','r',encoding='utf8') as fichierMb:
    fichierMb = fichierMb.read()

listLignesMb = fichierMb.split("\n")
listMembres = list()

i= 0
while i < len(listLignesMb):
    listInfosMb = listLignesMb[i].split(";")
    listMembres.append(Membres(listInfosMb[0], listInfosMb[1], listInfosMb[2], listInfosMb[3]))
    i+=1


for Membres in listMembres:
    sql = "INSERT INTO membres(nom, prenom, eMail, gMail)\
        VALUES ('%s', '%s', '%s', '%s')" %\
          (Membres.nom, Membres.prenom, Membres.eMail, Membres.gMail)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


db.close()