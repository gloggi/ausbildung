# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Notfallblatt'
        db.create_table('anmeldung_notfallblatt', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('anmeldung', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anmeldung.Anmeldung'], unique=True)),
            ('kontakt', self.gf('ausbildung.anmeldung.fields.RequiredCharField')(max_length=100)),
            ('strasse', self.gf('ausbildung.anmeldung.fields.RequiredCharField')(max_length=100)),
            ('plz', self.gf('django.db.models.fields.IntegerField')()),
            ('ort', self.gf('ausbildung.anmeldung.fields.RequiredCharField')(max_length=100)),
            ('land', self.gf('ausbildung.anmeldung.fields.RequiredCharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('telefon', self.gf('ausbildung.anmeldung.fields.OptionalCharField')(max_length=100, null=True, blank=True)),
            ('mobiltelefon', self.gf('ausbildung.anmeldung.fields.OptionalCharField')(max_length=100, null=True, blank=True)),
            ('krankenkasse', self.gf('ausbildung.anmeldung.fields.RequiredCharField')(max_length=100)),
            ('rega', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('arzt_name', self.gf('ausbildung.anmeldung.fields.RequiredCharField')(max_length=100)),
            ('arzt_strasse', self.gf('ausbildung.anmeldung.fields.RequiredCharField')(max_length=100)),
            ('arzt_plz', self.gf('django.db.models.fields.IntegerField')()),
            ('arzt_ort', self.gf('ausbildung.anmeldung.fields.RequiredCharField')(max_length=100)),
            ('arzt_telefon', self.gf('ausbildung.anmeldung.fields.RequiredCharField')(max_length=100)),
            ('starrkramp', self.gf('ausbildung.anmeldung.fields.RequiredCharField')(max_length=100)),
            ('medikamente', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('medis_ll', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('gesundheitszustand', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('weiteres', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('anmeldung', ['Notfallblatt'])

        # Deleting field 'Anmeldung.notfallblatt'
        db.delete_column('anmeldung_anmeldung', 'notfallblatt')

        # Deleting field 'Anmeldung.seki'
        db.delete_column('anmeldung_anmeldung', 'seki')

        # Adding field 'Anmeldung.anmeldung_erhalten'
        db.add_column('anmeldung_anmeldung', 'anmeldung_erhalten',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Anmeldung.notfallblatt_erhalten'
        db.add_column('anmeldung_anmeldung', 'notfallblatt_erhalten',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Notfallblatt'
        db.delete_table('anmeldung_notfallblatt')

        # Adding field 'Anmeldung.notfallblatt'
        db.add_column('anmeldung_anmeldung', 'notfallblatt',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Anmeldung.seki'
        db.add_column('anmeldung_anmeldung', 'seki',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Anmeldung.anmeldung_erhalten'
        db.delete_column('anmeldung_anmeldung', 'anmeldung_erhalten')

        # Deleting field 'Anmeldung.notfallblatt_erhalten'
        db.delete_column('anmeldung_anmeldung', 'notfallblatt_erhalten')


    models = {
        'anmeldung.abteilung': {
            'Meta': {'object_name': 'Abteilung'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'max_length': '100'}),
            'region': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'max_length': '100'}),
            'verband': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'default': "'ZH'", 'max_length': '100'})
        },
        'anmeldung.anmeldung': {
            'Meta': {'unique_together': "(('kurs', 'user'),)", 'object_name': 'Anmeldung'},
            'abteilung': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anmeldung.Abteilung']"}),
            'ahv': ('ausbildung.anmeldung.fields.OptionalCharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'anmeldung_erhalten': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'bahnabo': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'default': "'Keines'", 'max_length': '100'}),
            'bestaetigung': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bezahlt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'einheit': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'erstsprache': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'default': "''", 'max_length': '100'}),
            'foto': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'geburtsdatum': ('django.db.models.fields.DateField', [], {}),
            'geschlecht': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'js': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'kurs': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'anmeldungen'", 'to': "orm['anmeldung.Kurs']"}),
            'land': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'default': "'CH'", 'max_length': '100'}),
            'mobiltelefon': ('ausbildung.anmeldung.fields.OptionalCharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nachname': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'max_length': '100'}),
            'nationalitaet': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'default': "'CH'", 'max_length': '100'}),
            'notfallblatt_erhalten': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'ort': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'max_length': '100'}),
            'pfadiname': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'max_length': '100'}),
            'plz': ('django.db.models.fields.IntegerField', [], {}),
            'schweinefleisch': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'strasse': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'max_length': '100'}),
            'stufe': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'max_length': '100'}),
            'telefon': ('ausbildung.anmeldung.fields.OptionalCharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'anmeldungen'", 'to': "orm['auth.User']"}),
            'vegetarier': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vorname': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'max_length': '100'})
        },
        'anmeldung.kurs': {
            'Meta': {'object_name': 'Kurs'},
            'aktualisiert': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'anmeldeschluss': ('django.db.models.fields.DateField', [], {}),
            'bis': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'erfasst': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hauptleiter': ('ausbildung.anmeldung.fields.OptionalCharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'max_length': '100'}),
            'nummer': ('ausbildung.anmeldung.fields.OptionalCharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'teilnehmer': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'through': "orm['anmeldung.Anmeldung']", 'symmetrical': 'False'}),
            'url': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'von': ('django.db.models.fields.DateField', [], {})
        },
        'anmeldung.notfallblatt': {
            'Meta': {'object_name': 'Notfallblatt'},
            'anmeldung': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anmeldung.Anmeldung']", 'unique': 'True'}),
            'arzt_name': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'max_length': '100'}),
            'arzt_ort': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'max_length': '100'}),
            'arzt_plz': ('django.db.models.fields.IntegerField', [], {}),
            'arzt_strasse': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'max_length': '100'}),
            'arzt_telefon': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'gesundheitszustand': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kontakt': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'max_length': '100'}),
            'krankenkasse': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'max_length': '100'}),
            'land': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'max_length': '100'}),
            'medikamente': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'medis_ll': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mobiltelefon': ('ausbildung.anmeldung.fields.OptionalCharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ort': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'max_length': '100'}),
            'plz': ('django.db.models.fields.IntegerField', [], {}),
            'rega': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'starrkramp': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'max_length': '100'}),
            'strasse': ('ausbildung.anmeldung.fields.RequiredCharField', [], {'max_length': '100'}),
            'telefon': ('ausbildung.anmeldung.fields.OptionalCharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'weiteres': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['anmeldung']