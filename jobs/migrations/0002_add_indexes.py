# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Study', fields ['completed']
        db.create_index('jobs_study', ['completed'])

        # Adding index on 'Application', fields ['key']
        db.create_index('jobs_application', ['key'])

        # Adding index on 'WorkExperience', fields ['start_date']
        db.create_index('jobs_workexperience', ['start_date'])


    def backwards(self, orm):
        # Removing index on 'WorkExperience', fields ['start_date']
        db.delete_index('jobs_workexperience', ['start_date'])

        # Removing index on 'Application', fields ['key']
        db.delete_index('jobs_application', ['key'])

        # Removing index on 'Study', fields ['completed']
        db.delete_index('jobs_study', ['completed'])


    models = {
        'jobs.application': {
            'Meta': {'object_name': 'Application'},
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'employer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['jobs.Employer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '256', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pages': ('sortedm2m.fields.SortedManyToManyField', [], {'to': "orm['jobs.ApplicationPage']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'jobs.applicationpage': {
            'Meta': {'object_name': 'ApplicationPage'},
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'jobs.employer': {
            'Meta': {'object_name': 'Employer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'jobs.genericcontent': {
            'Meta': {'object_name': 'GenericContent'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'jobs.link': {
            'Meta': {'object_name': 'Link'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'network': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'jobs.reference': {
            'Meta': {'object_name': 'Reference'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'jobs.skill': {
            'Meta': {'object_name': 'Skill'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'jobs.study': {
            'Meta': {'ordering': "('-completed',)", 'object_name': 'Study'},
            'completed': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 7, 11, 0, 0)', 'db_index': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'jobs.workexperience': {
            'Meta': {'ordering': "('-start_date',)", 'object_name': 'WorkExperience'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 7, 11, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 7, 11, 0, 0)', 'db_index': 'True'})
        }
    }

    complete_apps = ['jobs']