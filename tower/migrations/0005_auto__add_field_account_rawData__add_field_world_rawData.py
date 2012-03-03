# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Account.rawData'
        db.add_column('tower_account', 'rawData', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'World.rawData'
        db.add_column('tower_world', 'rawData', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Account.rawData'
        db.delete_column('tower_account', 'rawData')

        # Deleting field 'World.rawData'
        db.delete_column('tower_world', 'rawData')


    models = {
        'tower.account': {
            'Meta': {'object_name': 'Account'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'pushID': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'rawData': ('django.db.models.fields.TextField', [], {}),
            'worlds': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tower.World']", 'symmetrical': 'False'})
        },
        'tower.world': {
            'Meta': {'object_name': 'World'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nextTurn': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'rawData': ('django.db.models.fields.TextField', [], {}),
            'turnData': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['tower']
