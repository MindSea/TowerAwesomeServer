# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding M2M table for field worlds on 'Account'
        db.create_table('tower_account_worlds', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('account', models.ForeignKey(orm['tower.account'], null=False)),
            ('world', models.ForeignKey(orm['tower.world'], null=False))
        ))
        db.create_unique('tower_account_worlds', ['account_id', 'world_id'])

        # Deleting field 'World.currentTurn'
        db.delete_column('tower_world', 'currentTurn')

        # Adding field 'World.turnData'
        db.add_column('tower_world', 'turnData', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Removing M2M table for field players on 'World'
        db.delete_table('tower_world_players')


    def backwards(self, orm):
        
        # Removing M2M table for field worlds on 'Account'
        db.delete_table('tower_account_worlds')

        # Adding field 'World.currentTurn'
        db.add_column('tower_world', 'currentTurn', self.gf('django.db.models.fields.IntegerField')(default=''), keep_default=False)

        # Deleting field 'World.turnData'
        db.delete_column('tower_world', 'turnData')

        # Adding M2M table for field players on 'World'
        db.create_table('tower_world_players', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('world', models.ForeignKey(orm['tower.world'], null=False)),
            ('player', models.ForeignKey(orm['tower.player'], null=False))
        ))
        db.create_unique('tower_world_players', ['world_id', 'player_id'])


    models = {
        'tower.account': {
            'Meta': {'object_name': 'Account'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'pushID': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'worlds': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tower.World']", 'symmetrical': 'False'})
        },
        'tower.actions': {
            'Meta': {'object_name': 'Actions'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locationX': ('django.db.models.fields.FloatField', [], {}),
            'locationY': ('django.db.models.fields.FloatField', [], {})
        },
        'tower.building': {
            'Meta': {'object_name': 'Building'},
            'baseX': ('django.db.models.fields.FloatField', [], {}),
            'baseY': ('django.db.models.fields.FloatField', [], {}),
            'buildingType': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'health': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tower.player': {
            'Meta': {'object_name': 'Player'},
            'account': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tower.Account']", 'symmetrical': 'False'}),
            'buildings': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tower.Building']", 'symmetrical': 'False'}),
            'gold': ('django.db.models.fields.IntegerField', [], {}),
            'health': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locationX': ('django.db.models.fields.FloatField', [], {}),
            'locationY': ('django.db.models.fields.FloatField', [], {})
        },
        'tower.turn': {
            'Meta': {'object_name': 'Turn'},
            'actions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tower.Building']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nextTurn': ('django.db.models.fields.IntegerField', [], {})
        },
        'tower.world': {
            'Meta': {'object_name': 'World'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'turnData': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['tower']
