from django.db import models
from . import enum
from django.utils.translation import ugettext as _

class TipoEtichetta(enum.Enumeration):
    intero = enum.Item(1, 'integer', 'Integer')
    stringa = enum.Item(2, 'string', 'Text')
    booleano = enum.Item(3, 'boolean', 'Y/N')


class Etichetta(models.Model):
    nome = models.CharField(max_length=255, verbose_name=_("Nome"))
    tipo = enum.EnumField(TipoEtichetta, verbose_name=_("Tipo"))

    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name = _('Etichetta')
        verbose_name_plural = _('Etichette')
    
class Persona(models.Model):
    cognome = models.CharField(max_length=255, verbose_name=_("Cognome"))
    nome = models.CharField(max_length=255, blank=True, verbose_name=_("Nome"))
    email = models.EmailField(blank=True, verbose_name=_("Email"))
    fax = models.CharField(max_length=255, blank=True, verbose_name="Fax")
    telefono1 = models.CharField(max_length=255, blank=True, verbose_name="Tel. 1")
    telefono2 = models.CharField(max_length=255, blank=True, verbose_name="Tel. 2")
    codice1 = models.CharField(max_length=255, verbose_name=_("Codice"), blank=True)
    codiceco = models.CharField(max_length=255, verbose_name=_("Cod.2"), blank=True)
    codicecs = models.CharField(max_length=255, verbose_name=_("Cod.3"), blank=True)
    etichette = models.ManyToManyField(Etichetta, blank=True, verbose_name=_("Etichette"))
    
    class Meta:
        verbose_name = _('Persona')
        verbose_name_plural = _('Persone')
