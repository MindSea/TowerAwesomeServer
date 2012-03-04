# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Account.id'
        db.delete_column('tower_account', 'id')

        # Changing field 'Account.email'
        db.alter_column('tower_account', 'email', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True))

        # Adding unique constraint on 'Account', fields ['email']
        db.create_unique('tower_account', ['email'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Account', fields ['email']
        db.delete_unique('tower_account', ['email'])

        # User chose to not deal with backwards NULL issues for 'Account.id'
        raise RuntimeError("Cannot reverse this migration. 'Account.id' and its values cannot be restored.")

        # Changing field 'Account.email'
        db.alter_column('tower_account', 'email', self.gf('django.db.models.fields.CharField')(max_length=256))


    models = {
        'tower.account': {
            'Meta': {'object_name': 'Account'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'pushID': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'rawData': ('django.db.models.fields.TextField', [], {}),
            'worlds': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tower.World']", 'symmetrical': 'False'})
        },
        'tower.world': {
            'Meta': {'object_name': 'World'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastTurn': ('django.db.models.fields.TextField', [], {}),
            'nextTurn': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'rawData': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['tower']
