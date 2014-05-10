from random import randint
import re

fnomi = open("nomi", "r")
fcognomi = open("cognomi", "r")

print "from app.models import Persona"

for i in range(400):
    nome = " ".join(re.findall("[a-zA-Z]+", fnomi.readline().split(",")[1][1:-2]))
    cognome = " ".join(re.findall("[a-zA-Z]+", fcognomi.readline().split(",")[1][1:-2]))
    fax = "0" + str(randint(1000000, 20000000))
    telefono1 = "0" + str(randint(1000000, 20000000))
    telefono2 = "0" + str(randint(1000000, 20000000))
    codice1 = randint(100, 999)
    email = nome.lower() + cognome.lower() + "@example.com"

    q = "p = Persona(nome='%s', cognome='%s', email='%s', fax='%s', telefono1='%s', telefono2='%s', codice1='%s')" % (nome, cognome, email, fax, telefono1, telefono2, codice1)
    print q
    print "p.save()"

fnomi.close()
fcognomi.close()
