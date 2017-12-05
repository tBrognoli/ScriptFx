import pymysql

db = pymysql.connect("localhost", "root", "", "numelops")

cursor = db.cursor()

sql = """CREATE TABLE Membres (
    id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nom char(25) NOT NULL,
    Prenom char(25) NOT NULL,
    eMail char(50),
    gMail char(50) )"""

cursor.execute(sql)

db.close()