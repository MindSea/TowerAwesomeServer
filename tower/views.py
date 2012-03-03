from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from tower.models import Account
from django.utils import simplejson
from django.core import serializers
from urllib import urlencode
import urlparse


def accounts(request, email):
    account = Account.objects.get(email=email)
    
    account = {
        'account': {
            'pushID': account.pushID,
            'name': account.name,
            'email': account.email,
        }
    }
    
    out = simplejson.dumps([account])
    
    return HttpResponse(out, mimetype="application/json")


def worlds(request, id):
    pass


#     return HttpResponse(json.dumps(response_data), mimetype="application/json")
