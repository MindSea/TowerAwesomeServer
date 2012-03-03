# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Actions'
        db.delete_table('tower_actions')

        # Deleting model 'Turn'
        db.delete_table('tower_turn')

        # Removing M2M table for field actions on 'Turn'
        db.delete_table('tower_turn_actions')

        # Deleting model 'Player'
        db.delete_table('tower_player')

        # Removing M2M table for field account on 'Player'
        db.delete_table('tower_player_account')

        # Removing M2M table for field buildings on 'Player'
        db.delete_table('tower_player_buildings')

        # Deleting model 'Building'
        db.delete_table('tower_building')

        # Adding M2M table for field nextTurn on 'World'
        db.create_table('tower_world_nextTurn', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('world', models.ForeignKey(orm['tower.world'], null=False)),
            ('account', models.ForeignKey(orm['tower.account'], null=False))
        ))
        db.create_unique('tower_world_nextTurn', ['world_id', 'account_id'])


    def backwards(self, orm):
        
        # Adding model 'Actions'
        db.create_table('tower_actions', (
            ('action', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('locationX', self.gf('django.db.models.fields.FloatField')()),
            ('locationY', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('tower', ['Actions'])

        # Adding model 'Turn'
        db.create_table('tower_turn', (
            ('nextTurn', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('tower', ['Turn'])

        # Adding M2M table for field actions on 'Turn'
        db.create_table('tower_turn_actions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('turn', models.ForeignKey(orm['tower.turn'], null=False)),
            ('building', models.ForeignKey(orm['tower.building'], null=False))
        ))
        db.create_unique('tower_turn_actions', ['turn_id', 'building_id'])

        # Adding model 'Player'
        db.create_table('tower_player', (
            ('health', self.gf('django.db.models.fields.IntegerField')()),
            ('locationX', self.gf('django.db.models.fields.FloatField')()),
            ('gold', self.gf('django.db.models.fields.IntegerField')()),
            ('locationY', self.gf('django.db.models.fields.FloatField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('tower', ['Player'])

        # Adding M2M table for field account on 'Player'
        db.create_table('tower_player_account', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('player', models.ForeignKey(orm['tower.player'], null=False)),
            ('account', models.ForeignKey(orm['tower.account'], null=False))
        ))
        db.create_unique('tower_player_account', ['player_id', 'account_id'])

        # Adding M2M table for field buildings on 'Player'
        db.create_table('tower_player_buildings', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('player', models.ForeignKey(orm['tower.player'], null=False)),
            ('building', models.ForeignKey(orm['tower.building'], null=False))
        ))
        db.create_unique('tower_player_buildings', ['player_id', 'building_id'])

        # Adding model 'Building'
        db.create_table('tower_building', (
            ('health', self.gf('django.db.models.fields.IntegerField')()),
            ('baseX', self.gf('django.db.models.fields.FloatField')()),
            ('baseY', self.gf('django.db.models.fields.FloatField')()),
            ('buildingType', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('tower', ['Building'])

        # Removing M2M table for field nextTurn on 'World'
        db.delete_table('tower_world_nextTurn')


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
            'nextTurn': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tower.Account']", 'symmetrical': 'False'}),
            'turnData': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['tower']
