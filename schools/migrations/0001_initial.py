# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'School'
        db.create_table('schools_school', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('schools', ['School'])

        # Adding model 'SchoolAddress'
        db.create_table('schools_schooladdress', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(related_name='addresses', to=orm['schools.School'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.contrib.localflavor.us.models.USStateField')(max_length=2)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('phone_number', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal('schools', ['SchoolAddress'])

        # Adding model 'Class'
        db.create_table('schools_class', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(related_name='classes', to=orm['schools.School'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=11, decimal_places=2)),
        ))
        db.send_create_signal('schools', ['Class'])

        # Adding model 'Schedule'
        db.create_table('schools_schedule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school_class', self.gf('django.db.models.fields.related.ForeignKey')(related_name='class_schedules', to=orm['schools.Class'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('num_meetings', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('max_students', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('schools', ['Schedule'])

        # Adding model 'Instructor'
        db.create_table('schools_instructor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('schedule', self.gf('django.db.models.fields.related.ForeignKey')(related_name='instructors', to=orm['schools.Schedule'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('bio', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('schools', ['Instructor'])


    def backwards(self, orm):
        # Deleting model 'School'
        db.delete_table('schools_school')

        # Deleting model 'SchoolAddress'
        db.delete_table('schools_schooladdress')

        # Deleting model 'Class'
        db.delete_table('schools_class')

        # Deleting model 'Schedule'
        db.delete_table('schools_schedule')

        # Deleting model 'Instructor'
        db.delete_table('schools_instructor')


    models = {
        'schools.class': {
            'Meta': {'object_name': 'Class'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '11', 'decimal_places': '2'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'classes'", 'to': "orm['schools.School']"})
        },
        'schools.instructor': {
            'Meta': {'object_name': 'Instructor'},
            'bio': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instructors'", 'to': "orm['schools.Schedule']"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'schools.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_students': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'num_meetings': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'school_class': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'class_schedules'", 'to': "orm['schools.Class']"}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        'schools.school': {
            'Meta': {'object_name': 'School'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'schools.schooladdress': {
            'Meta': {'object_name': 'SchoolAddress'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_number': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'addresses'", 'to': "orm['schools.School']"}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['schools']