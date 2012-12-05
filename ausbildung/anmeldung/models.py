# encoding: utf-8

from django.db import models
from django.utils.timezone import now

from sorl.thumbnail import ImageField

from .fields import RequiredCharField, OptionalCharField

import reversion

class KursManager(models.Manager):
    def open(self):
        return self.get_query_set().filter(anmeldeschluss__gte=now())


class Kurs(models.Model):
    name = RequiredCharField('Name')
    url = models.SlugField('url')

    nummer = OptionalCharField('Kursnummer', help_text='z.Bsp PBS ZH 123-12')

    von = models.DateField('Von')
    bis = models.DateField('Bis')
    anmeldeschluss = models.DateField('Anmeldeschluss')

    hauptleiter = OptionalCharField('Hauptleiter')
    email = models.EmailField('Email', blank=True, null=True)

    erfasst = models.DateTimeField('Erfasst', auto_now_add=True)
    aktualisiert = models.DateTimeField('Aktualisiert', auto_now=True)

    teilnehmer = models.ManyToManyField('auth.User', through='Anmeldung')

    objects = KursManager()

    class Meta:
        verbose_name = 'Kurs'
        verbose_name_plural = 'Kurse'

    def __unicode__(self):
        return self.name

    @property
    def foo(self, erwin):
        pass


class Abteilung(models.Model):

    verband = RequiredCharField('Kantonalverband', default='ZH')
    region = RequiredCharField('Region / Korps')
    name = RequiredCharField('Abteilungsname')

    class Meta:
        verbose_name = 'Abteilung'
        verbose_name_plural = 'Abteilungen'

    def __unicode__(self):
        return u'%s - %s' % (self.region, self.name)


class Anmeldung(models.Model):

    GESCHLECHT_CHOICES = (
        ('1', u'männlich'),
        ('2', u'weiblich'),
    )

    LAND_CHOICES = (
        ('CH', 'Schweiz'),
        ('FL', 'Fürstentum Lichtenstein'),
        ('D', 'Deutschland'),
        ('F', 'Frankreich'),
        ('I', 'Italien'),
        ('A', 'Österreich'),
    )

    ERSTSPRACHE_CHOICES = (
        ('D', u'Deutsch'),
        ('F', u'Französisch'),
        ('I', u'Italienisch'),
        ('E', u'Englisch'),
    )

    BAHNABO_CHOICES = (
        ('Keines', u'Keines'),
        ('GA', u'GA'),
        ('Halbtax', u'Halbtax'),
        ('Regenbogen', u'Regenbogen'),
        ('Gleis 7', u'Gleis 7'),
    )

    STUFE_CHOICES = (
        ('biber', u'Biberstufe'),
        ('wolf', u'Wolfsstufe'),
        ('pfadi', u'Pfadistufe'),
        ('pio', u'Piostufe'),
        ('rover', u'Roverstufe'),
    )

    kurs = models.ForeignKey(Kurs, related_name='anmeldungen')
    user = models.ForeignKey('auth.User', related_name='anmeldungen')

    # Adminfelder

    seki = models.DateTimeField('Unterschriebene Anmeldung erhalten',
        blank=True, null=True)
    notfallblatt = models.DateTimeField('Notfallblatt erhalten', blank=True,
        null=True)
    bezahlt = models.DateTimeField('Zahlung eingegangen', blank=True, null=True)


    # Personendaten

    pfadiname = RequiredCharField('Pfadiname')
    vorname = RequiredCharField('Vorname')
    nachname = RequiredCharField('Nachname')
    geschlecht = RequiredCharField('Geschlecht', choices=GESCHLECHT_CHOICES)
    geburtsdatum = models.DateField('Geburtsdatum')

    foto = ImageField('Foto', upload_to="tnfotos", blank=True, null=True)

    strasse = RequiredCharField('Strasse')
    plz = models.IntegerField('PLZ')
    ort = RequiredCharField('Ort')
    land = RequiredCharField('Land', choices=LAND_CHOICES, default='CH')

    email = models.EmailField('Email')
    telefon = OptionalCharField('Telefon')
    mobiltelefon = OptionalCharField('Natel')

    # Pfadizugehörigkeit
    abteilung = models.ForeignKey(Abteilung, verbose_name='Abteilung')
    einheit = RequiredCharField('Einheit')
    stufe = RequiredCharField('Stufe', choices=STUFE_CHOICES)


    nationalitaet = RequiredCharField(u'Nationalität', default='CH')
    erstsprache = RequiredCharField('Erstsprache', choices=ERSTSPRACHE_CHOICES,
        default='')
    bahnabo = RequiredCharField('Bahnabo', choices=BAHNABO_CHOICES,
        default='Keines')


    js = models.IntegerField('JS-Nummer', blank=True, null=True)
    ahv = OptionalCharField('AHV-Nr.')

    vegetarier = models.BooleanField('Vegetarier',
        help_text="Ich bin Vegetarier"
    )
    schweinefleisch = models.BooleanField('Kein Schweinefleich',
        help_text="Ich esse kein Schweinefleich"
    )

    bestaetigung = models.BooleanField('Bestätigung',
        help_text=u'Ich benötige eine Bestätigung für meinen Arbeitsgeber')

    class Meta:
        verbose_name = 'Ammeldung'
        verbose_name_plural = 'Anmeldungen'
        unique_together = (('kurs', 'user'),)

    def __unicode__(self):
        return u'%s %s v/o %s' % (self.vorname, self.nachname, self.pfadiname)
