from django.db import models


class Account(models.Model):
    name = models.CharField('Name', max_length=256)
    email = models.CharField('Email', max_length=256)
    pushID = models.CharField('PushID', max_length=256)
    worlds = models.ManyToManyField('World')
    
    def __unicode__(self):
        return self.name + " - " + self.email


class World(models.Model):
    turnData = models.TextField('Turn data')
    nextTurn = models.CharField('Email', max_length=256)
    
    def __unicode__(self):
        return "World - " + str(self.pk)


"""

For an account, give me all the worlds

from tower.models import Account
a = Account.objects.all()
a[0].worlds.all()

"""