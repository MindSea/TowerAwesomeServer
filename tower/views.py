from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from tower.models import Account, World
from django.utils import simplejson
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
            }
        }
        
        out = simplejson.dumps([accountData])
        
        return HttpResponse(out, mimetype="application/json")
    elif request.method == 'POST':
        a = Account(
            name = request.POST['name'],
            email = request.POST['email'],
            pushID = request.POST['pushID'],
        )
        
        a.save()
        
        return HttpResponse({}, mimetype="application/json")


def worldList(request, email=''):
    account = Account.objects.get(email=email)
    
    worlds = []
    
    for w in account.worlds.all():
        worlds.append({
            'turnData': w.turnData,
            'nextTurn': w.nextTurn,
        })
    
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
                'turnData': world.turnData,
                'nextTurn': nextTurn,
            }
        }
        
        out = simplejson.dumps([worldData])
        
        return HttpResponse(out, mimetype="application/json")
    elif request.method == 'POST':
        if ('id' in request.POST):
            w = World(
                id = request.POST['id'],
                turnData = request.POST['turnData'],
                nextTurn = request.POST['nextTurn'],
            )
        else:
            w = World(
                turnData = request.POST['turnData'],
                nextTurn = request.POST['nextTurn'],
            )
        
        w.save()
        
        data = {
            'id': w.id
        }
        
        out = simplejson.dumps([data])
        
        return HttpResponse(out, mimetype="application/json")





#     return HttpResponse(json.dumps(response_data), mimetype="application/json")
