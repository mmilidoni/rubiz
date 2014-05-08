from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', 'app.views.elenco_persone'),
        url(r'^login$', 'app.views.userlogin'),
        url(r'^logout$', 'app.views.userlogout'),

        url(r'^stampa_elenco/$', 'app.views.stampa_elenco'),
        url(r'^stampa_rubrica/$', 'app.views.stampa_rubrica'),
        url(r'^stampa_etichette/$', 'app.views.stampa_etichette'),
        url(r'^form_stampa/(?P<tipo>elenco)/$', 'app.views.form_stampa'),
        url(r'^form_stampa/(?P<tipo>rubrica)/$', 'app.views.form_stampa'),
        url(r'^form_stampa/(?P<tipo>etichette)/$', 'app.views.form_stampa'),

        url(r'^elenco_persone$', 'app.views.elenco_persone'),
        url(r'^nuova_persona$', 'app.views.form_persona'),
        url(r'^form_persona/$', 'app.views.form_persona'),
        url(r'^form_persona/(?P<pk>\d+)/$', 'app.views.form_persona'),
        url(r'^elimina_persona/(?P<pk>[\d]+)/$', 'app.views.elimina_persona'),

        url(r'^elenco_etichette$', 'app.views.elenco_etichette'),
        url(r'^nuova_etichetta$', 'app.views.form_etichetta'),
        url(r'^form_etichetta/$', 'app.views.form_etichetta'),
        url(r'^form_etichetta/(?P<pk>\d+)/$', 'app.views.form_etichetta'),
        url(r'^elimina_etichetta/(?P<pk>[\d]+)/$', 'app.views.elimina_etichetta'),

    # Examples:
    # url(r'^$', 'rubiz.views.home', name='home'),
    # url(r'^rubiz/', include('rubiz.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
