from django.db import models


class Account(models.Model):
    name = models.CharField('Name', max_length=256)
    email = models.CharField('Email', max_length=255, primary_key=True)
    pushID = models.CharField('PushID', max_length=256)
    worlds = models.ManyToManyField('World')
    rawData = models.TextField('Raw JSON data')
    
    def __unicode__(self):
        return self.name + " - " + self.email


class World(models.Model):
    lastTurn = models.TextField('Turn data')
    nextTurn = models.CharField('Email', max_length=256)
    rawData = models.TextField('Raw JSON data')
    
    def __unicode__(self):
        return "World - " + str(self.pk)


"""

For an account, give me all the worlds

from tower.models import Account
a = Account.objects.all()
a[0].worlds.all()

"""