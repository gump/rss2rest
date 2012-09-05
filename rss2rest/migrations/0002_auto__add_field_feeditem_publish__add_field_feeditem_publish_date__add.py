# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FeedItem.publish'
        db.add_column('rss2rest_feeditem', 'publish',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'FeedItem.publish_date'
        db.add_column('rss2rest_feeditem', 'publish_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 9, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'VimeoFeedItem.publish'
        db.add_column('rss2rest_vimeofeeditem', 'publish',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'VimeoFeedItem.publish_date'
        db.add_column('rss2rest_vimeofeeditem', 'publish_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 9, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'PictureFeedItem.publish'
        db.add_column('rss2rest_picturefeeditem', 'publish',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'PictureFeedItem.publish_date'
        db.add_column('rss2rest_picturefeeditem', 'publish_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 9, 5, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'FeedItem.publish'
        db.delete_column('rss2rest_feeditem', 'publish')

        # Deleting field 'FeedItem.publish_date'
        db.delete_column('rss2rest_feeditem', 'publish_date')

        # Deleting field 'VimeoFeedItem.publish'
        db.delete_column('rss2rest_vimeofeeditem', 'publish')

        # Deleting field 'VimeoFeedItem.publish_date'
        db.delete_column('rss2rest_vimeofeeditem', 'publish_date')

        # Deleting field 'PictureFeedItem.publish'
        db.delete_column('rss2rest_picturefeeditem', 'publish')

        # Deleting field 'PictureFeedItem.publish_date'
        db.delete_column('rss2rest_picturefeeditem', 'publish_date')


    models = {
        'rss2rest.feeditem': {
            'Meta': {'object_name': 'FeedItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {}),
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
            'publish_date': ('django.db.models.fields.DateTimeField', [], {}),
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
            'publish_date': ('django.db.models.fields.DateTimeField', [], {}),
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