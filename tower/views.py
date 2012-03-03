from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from tower.models import Account, World
from django.utils import simplejson
import json
from django.core import serializers
from urllib import urlencode
import urlparse


def accounts(request, email=''):
    if request.method == 'GET':
        account = Account.objects.get(email=email)
        
        worlds = []
        
        for w in account.worlds.all():
            worlds.append(w.pk)
        
        accountData = {
            'account': {
                'pushID': account.pushID,
                'name': account.name,
                'email': account.email,
                'worlds': worlds,
                'rawData': account.rawData,
            }
        }
        
        out = simplejson.dumps([accountData])
        
        return HttpResponse(out, mimetype="application/json")
    elif request.method == 'POST':
        jsonData = request.raw_post_data
        
        data = json.loads(jsonData)
        
        a = Account(
            name = data['name'],
            email = data['email'],
            pushID = data['pushID'],
            rawData = jsonData,
        )
        
        a.save()
        
        return HttpResponse({}, mimetype="application/json")


def worldList(request, email=''):
    account = Account.objects.get(email=email)
    
    worlds = []
    
    for w in account.worlds.all():
        worlds.append(json.loads(w.rawData))
    
    worldList = {
        'worlds': worlds,
    }
    
    out = simplejson.dumps(worldList)
    
    return HttpResponse(out, mimetype="application/json")


def worlds(request, id=''):
    if request.method == 'GET':
        world = World.objects.get(pk=id)
        
        if world.nextTurn:
            nextTurn = world.nextTurn
        else:
            nextTurn = False
        
        worldData = {
            'world': {
                'lastTurn': world.lastTurn,
                'nextTurn': nextTurn,
                'rawData': world.rawData,
            }
        }
        
        out = simplejson.dumps([worldData])
        
        return HttpResponse(out, mimetype="application/json")
    elif request.method == 'POST':
        jsonData = request.raw_post_data
        
        data = json.loads(jsonData)
        
        # a = Account.objects.get(email)
        
        if ('id' in request.POST):
            w = World(
                id = data['id'],
                lastTurn = data['lastTurn'],
                nextTurn = data['nextTurn'],
                rawData = jsonData,
            )
        else:
            w = World(
                lastTurn = data['lastTurn'],
                nextTurn = data['nextTurn'],
                rawData = jsonData,
            )
        
        w.save()
        
        for p in data['players']:
            accounts = Account.objects.all().filter(email=p['email'])
            
            for a in accounts:
                a.worlds.add(w)
        
        data['id'] = w.id
        
        out = simplejson.dumps({'worlds': data})
        
        return HttpResponse(out, mimetype="application/json")





#     return HttpResponse(json.dumps(response_data), mimetype="application/json")
