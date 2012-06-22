# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Employer'
        db.create_table('jobs_employer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('jobs', ['Employer'])

        # Adding model 'ApplicationPage'
        db.create_table('jobs_applicationpage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('attachment', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('jobs', ['ApplicationPage'])

        # Adding model 'Application'
        db.create_table('jobs_application', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('employer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jobs.Employer'])),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('attachment', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('jobs', ['Application'])


        # Adding SortedM2M table for field pages on 'Application'
        db.create_table('jobs_application_pages', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('application', models.ForeignKey(orm['jobs.application'], null=False)),
            ('applicationpage', models.ForeignKey(orm['jobs.applicationpage'], null=False)),
            ('sort_value', models.IntegerField())
        ))
        db.create_unique('jobs_application_pages', ['application_id', 'applicationpage_id'])
        # Adding model 'GenericContent'
        db.create_table('jobs_genericcontent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('jobs', ['GenericContent'])

        # Adding model 'WorkExperience'
        db.create_table('jobs_workexperience', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('start_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 6, 24, 0, 0))),
            ('end_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 6, 24, 0, 0), null=True, blank=True)),
        ))
        db.send_create_signal('jobs', ['WorkExperience'])

        # Adding model 'Study'
        db.create_table('jobs_study', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('completed', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 6, 24, 0, 0))),
        ))
        db.send_create_signal('jobs', ['Study'])

        # Adding model 'Reference'
        db.create_table('jobs_reference', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('jobs', ['Reference'])

        # Adding model 'Skill'
        db.create_table('jobs_skill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('jobs', ['Skill'])

        # Adding model 'Link'
        db.create_table('jobs_link', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('network', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('jobs', ['Link'])


    def backwards(self, orm):
        # Deleting model 'Employer'
        db.delete_table('jobs_employer')

        # Deleting model 'ApplicationPage'
        db.delete_table('jobs_applicationpage')

        # Deleting model 'Application'
        db.delete_table('jobs_application')

        # Removing M2M table for field pages on 'Application'
        db.delete_table('jobs_application_pages')

        # Deleting model 'GenericContent'
        db.delete_table('jobs_genericcontent')

        # Deleting model 'WorkExperience'
        db.delete_table('jobs_workexperience')

        # Deleting model 'Study'
        db.delete_table('jobs_study')

        # Deleting model 'Reference'
        db.delete_table('jobs_reference')

        # Deleting model 'Skill'
        db.delete_table('jobs_skill')

        # Deleting model 'Link'
        db.delete_table('jobs_link')


    models = {
        'jobs.application': {
            'Meta': {'object_name': 'Application'},
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'employer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['jobs.Employer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
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
            'completed': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 6, 24, 0, 0)'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'jobs.workexperience': {
            'Meta': {'ordering': "('-start_date',)", 'object_name': 'WorkExperience'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 6, 24, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 6, 24, 0, 0)'})
        }
    }

    complete_apps = ['jobs']