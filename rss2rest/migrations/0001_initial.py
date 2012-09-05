# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FeedItem'
        db.create_table('rss2rest_feeditem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source_id', self.gf('django.db.models.fields.CharField')(max_length=64, unique=True, null=True)),
            ('source_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('source_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('source_description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('source_author', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('source_thumbnail', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('source_pub_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('sync_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('rss2rest', ['FeedItem'])

        # Adding model 'VimeoFeedItem'
        db.create_table('rss2rest_vimeofeeditem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source_id', self.gf('django.db.models.fields.CharField')(max_length=64, unique=True, null=True)),
            ('source_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('source_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('source_description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('source_author', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('source_thumbnail', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('source_pub_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('sync_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('rss2rest', ['VimeoFeedItem'])

        # Adding model 'PictureFeedItem'
        db.create_table('rss2rest_picturefeeditem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source_id', self.gf('django.db.models.fields.CharField')(max_length=64, unique=True, null=True)),
            ('source_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('source_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('source_description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('source_author', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('source_thumbnail', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('source_pub_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('sync_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('rss2rest', ['PictureFeedItem'])

        # Adding model 'FlickrFeedItem'
        db.create_table('rss2rest_flickrfeeditem', (
            ('picturefeeditem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['rss2rest.PictureFeedItem'], unique=True, primary_key=True)),
            ('author_url', self.gf('django.db.models.fields.URLField')(max_length=255)),
        ))
        db.send_create_signal('rss2rest', ['FlickrFeedItem'])


    def backwards(self, orm):
        # Deleting model 'FeedItem'
        db.delete_table('rss2rest_feeditem')

        # Deleting model 'VimeoFeedItem'
        db.delete_table('rss2rest_vimeofeeditem')

        # Deleting model 'PictureFeedItem'
        db.delete_table('rss2rest_picturefeeditem')

        # Deleting model 'FlickrFeedItem'
        db.delete_table('rss2rest_flickrfeeditem')


    models = {
        'rss2rest.feeditem': {
            'Meta': {'object_name': 'FeedItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'source_description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'source_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'unique': 'True', 'null': 'True'}),
            'source_pub_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'source_thumbnail': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'source_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'source_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'sync_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'rss2rest.flickrfeeditem': {
            'Meta': {'object_name': 'FlickrFeedItem', '_ormbases': ['rss2rest.PictureFeedItem']},
            'author_url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'picturefeeditem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['rss2rest.PictureFeedItem']", 'unique': 'True', 'primary_key': 'True'})
        },
        'rss2rest.picturefeeditem': {
            'Meta': {'object_name': 'PictureFeedItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'source_description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'source_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'unique': 'True', 'null': 'True'}),
            'source_pub_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'source_thumbnail': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'source_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'source_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'sync_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'rss2rest.vimeofeeditem': {
            'Meta': {'object_name': 'VimeoFeedItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'source_description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'source_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'unique': 'True', 'null': 'True'}),
            'source_pub_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'source_thumbnail': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'source_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'source_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'sync_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rss2rest']