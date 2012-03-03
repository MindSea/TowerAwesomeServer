# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'World.nextTurn'
        db.add_column('tower_world', 'nextTurn', self.gf('django.db.models.fields.CharField')(default='', max_length=256), keep_default=False)

        # Removing M2M table for field nextTurn on 'World'
        db.delete_table('tower_world_nextTurn')


    def backwards(self, orm):
        
        # Deleting field 'World.nextTurn'
        db.delete_column('tower_world', 'nextTurn')

        # Adding M2M table for field nextTurn on 'World'
        db.create_table('tower_world_nextTurn', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('world', models.ForeignKey(orm['tower.world'], null=False)),
            ('account', models.ForeignKey(orm['tower.account'], null=False))
        ))
        db.create_unique('tower_world_nextTurn', ['world_id', 'account_id'])


    models = {
        'tower.account': {
            'Meta': {'object_name': 'Account'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'pushID': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'worlds': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tower.World']", 'symmetrical': 'False'})
        },
        'tower.world': {
            'Meta': {'object_name': 'World'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nextTurn': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'turnData': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['tower']
