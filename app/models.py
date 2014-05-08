from django.db import models
from . import enum

class TipoEtichetta(enum.Enumeration):
    intero = enum.Item(1, 'integer', 'Numero intero')
    stringa = enum.Item(2, 'string', 'Testo')
    booleano = enum.Item(3, 'boolean', 'Si/No')


class Etichetta(models.Model):
    nome = models.CharField(max_length=255)
    tipo = enum.EnumField(TipoEtichetta)

    def __unicode__(self):
        return self.nome
    
class Persona(models.Model):
    cognome = models.CharField(max_length=255)
    nome = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    fax = models.CharField(max_length=255, blank=True)
    telefono1 = models.CharField(max_length=255, blank=True)
    telefono2 = models.CharField(max_length=255, blank=True)
    codice1 = models.CharField(max_length=255, verbose_name=u"Codice Unico", blank=True)
    codiceco = models.CharField(max_length=255, verbose_name=u"Cod. Contab.", blank=True)
    codicecs = models.CharField(max_length=255, verbose_name=u"Cod. Sempl.", blank=True)
    etichette = models.ManyToManyField(Etichetta, blank=True)

