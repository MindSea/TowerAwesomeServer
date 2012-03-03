from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from tower.models import Account
# from django.utils import simplejson as json
from django.core import serializers


def accounts(request, email):
    account = Account.objects.all().filter(email=email)
    
    data = {
        'account': account,
    }
    
    out = serializers.serialize('json', data)
    
    print data
    
    return HttpResponse(out, mimetype="application/json")


#     return HttpResponse(json.dumps(response_data), mimetype="application/json")
