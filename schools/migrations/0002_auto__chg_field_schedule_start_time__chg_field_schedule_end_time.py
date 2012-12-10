# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Schedule.start_time'
        db.alter_column('schools_schedule', 'start_time', self.gf('django.db.models.fields.TimeField')())

        # Changing field 'Schedule.end_time'
        db.alter_column('schools_schedule', 'end_time', self.gf('django.db.models.fields.TimeField')())

    def backwards(self, orm):

        # Changing field 'Schedule.start_time'
        db.alter_column('schools_schedule', 'start_time', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Schedule.end_time'
        db.alter_column('schools_schedule', 'end_time', self.gf('django.db.models.fields.DateTimeField')())

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
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_students': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'num_meetings': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'school_class': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'class_schedules'", 'to': "orm['schools.Class']"}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
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