# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Account'
        db.create_table('tower_account', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('pushID', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('tower', ['Account'])

        # Adding model 'World'
        db.create_table('tower_world', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('currentTurn', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('tower', ['World'])

        # Adding M2M table for field players on 'World'
        db.create_table('tower_world_players', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('world', models.ForeignKey(orm['tower.world'], null=False)),
            ('player', models.ForeignKey(orm['tower.player'], null=False))
        ))
        db.create_unique('tower_world_players', ['world_id', 'player_id'])

        # Adding model 'Turn'
        db.create_table('tower_turn', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nextTurn', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('tower', ['Turn'])

        # Adding M2M table for field actions on 'Turn'
        db.create_table('tower_turn_actions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('turn', models.ForeignKey(orm['tower.turn'], null=False)),
            ('building', models.ForeignKey(orm['tower.building'], null=False))
        ))
        db.create_unique('tower_turn_actions', ['turn_id', 'building_id'])

        # Adding model 'Actions'
        db.create_table('tower_actions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('locationX', self.gf('django.db.models.fields.FloatField')()),
            ('locationY', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('tower', ['Actions'])

        # Adding model 'Player'
        db.create_table('tower_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('health', self.gf('django.db.models.fields.IntegerField')()),
            ('gold', self.gf('django.db.models.fields.IntegerField')()),
            ('locationX', self.gf('django.db.models.fields.FloatField')()),
            ('locationY', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('tower', ['Player'])

        # Adding M2M table for field buildings on 'Player'
        db.create_table('tower_player_buildings', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('player', models.ForeignKey(orm['tower.player'], null=False)),
            ('building', models.ForeignKey(orm['tower.building'], null=False))
        ))
        db.create_unique('tower_player_buildings', ['player_id', 'building_id'])

        # Adding M2M table for field account on 'Player'
        db.create_table('tower_player_account', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('player', models.ForeignKey(orm['tower.player'], null=False)),
            ('account', models.ForeignKey(orm['tower.account'], null=False))
        ))
        db.create_unique('tower_player_account', ['player_id', 'account_id'])

        # Adding model 'Building'
        db.create_table('tower_building', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('buildingType', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('baseX', self.gf('django.db.models.fields.FloatField')()),
            ('baseY', self.gf('django.db.models.fields.FloatField')()),
            ('health', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('tower', ['Building'])


    def backwards(self, orm):
        
        # Deleting model 'Account'
        db.delete_table('tower_account')

        # Deleting model 'World'
        db.delete_table('tower_world')

        # Removing M2M table for field players on 'World'
        db.delete_table('tower_world_players')

        # Deleting model 'Turn'
        db.delete_table('tower_turn')

        # Removing M2M table for field actions on 'Turn'
        db.delete_table('tower_turn_actions')

        # Deleting model 'Actions'
        db.delete_table('tower_actions')

        # Deleting model 'Player'
        db.delete_table('tower_player')

        # Removing M2M table for field buildings on 'Player'
        db.delete_table('tower_player_buildings')

        # Removing M2M table for field account on 'Player'
        db.delete_table('tower_player_account')

        # Deleting model 'Building'
        db.delete_table('tower_building')


    models = {
        'tower.account': {
            'Meta': {'object_name': 'Account'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'pushID': ('django.db.models.fields.CharField', [], {'max_length': '256'})
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
            'currentTurn': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'players': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tower.Player']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['tower']
