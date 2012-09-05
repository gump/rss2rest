# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'FeedItem.publish_date'
        db.alter_column('rss2rest_feeditem', 'publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'VimeoFeedItem.publish_date'
        db.alter_column('rss2rest_vimeofeeditem', 'publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'PictureFeedItem.publish_date'
        db.alter_column('rss2rest_picturefeeditem', 'publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):

        # Changing field 'FeedItem.publish_date'
        db.alter_column('rss2rest_feeditem', 'publish_date', self.gf('django.db.models.fields.DateTimeField')(default=False))

        # Changing field 'VimeoFeedItem.publish_date'
        db.alter_column('rss2rest_vimeofeeditem', 'publish_date', self.gf('django.db.models.fields.DateTimeField')(default=None))

        # Changing field 'PictureFeedItem.publish_date'
        db.alter_column('rss2rest_picturefeeditem', 'publish_date', self.gf('django.db.models.fields.DateTimeField')(default=None))

    models = {
        'rss2rest.feeditem': {
            'Meta': {'object_name': 'FeedItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
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
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
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
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
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