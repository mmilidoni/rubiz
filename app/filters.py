from app.models import Persona
import django_filters

class PersonaFilter(django_filters.FilterSet):
    cognome = django_filters.CharFilter(lookup_type = 'icontains')
    nome = django_filters.CharFilter(lookup_type = 'icontains')
    telefono1 = django_filters.CharFilter(lookup_type = 'icontains')
    telefono2 = django_filters.CharFilter(lookup_type = 'icontains')
    fax = django_filters.CharFilter(lookup_type = 'icontains')
    class Meta:
        model = Persona
        fields = ['cognome', 'nome', 'telefono1', 'telefono2', 'fax']
