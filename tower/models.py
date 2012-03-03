from django.db import models


class Account(models.Model):
    name = models.CharField('Name', max_length=256)
    email = models.CharField('Email', max_length=256)
    pushID = models.CharField('PushID', max_length=256)
    
    def __unicode__(self):
        return self.name + " - " + self.email


class World(models.Model):
    # worldID
    players = models.ManyToManyField('Player')
    currentTurn = models.IntegerField('Turn')


class Turn(models.Model):
    nextTurn = models.IntegerField('Next Turn')
    actions = models.ManyToManyField('Building')


class Actions(models.Model):
    action = models.CharField('Title', max_length=256)
    locationX = models.FloatField('Location X')
    locationY = models.FloatField('Location Y')


class Player(models.Model):
    health = models.IntegerField('Health')
    gold = models.IntegerField('Health')
    locationX = models.FloatField('Location X')
    locationY = models.FloatField('Location Y')
    buildings = models.ManyToManyField('Building')
    account = models.ManyToManyField('Account')
    
    class Meta:
        pass


class Building(models.Model):
    buildingType = models.CharField('Title', max_length=256)
    baseX = models.FloatField('Base X')
    baseY = models.FloatField('Base Y')
    health = models.IntegerField('Health')
    
    class Meta:
        pass



# Turn
#     - many actions
#         - type
#         - location


# Apply actions on next turn