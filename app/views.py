"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import Contact as modelContact
from django.db.models import Q
from django.http import HttpResponse
from django.core import serializers

def contact_manager(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact_manager.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact Manager',
            'year':datetime.now().year,
        })
    )

def all_contacts(request):
    contacts = serializers.serialize('json', modelContact.objects.all())
    return HttpResponse(contacts,content_type='json')

def insert_contact(request):
    con = modelContact()
    con.FirstName = request.GET['FirstName']
    con.LastName = request.GET['LastName']
    con.Email = request.GET['Email']
    con.Mobile = request.GET['Mobile']
    con.save()
    return HttpResponse(modelContact.objects.latest('id'))

def update_contact(request):
    con = modelContact()
    con.FirstName = request.GET['FirstName']
    con.LastName = request.GET['LastName']
    con.Email = request.GET['Email']
    con.Mobile = request.GET['Mobile']
    con.pk = request.GET['Id']
    con.save()
    return HttpResponse(modelContact.objects.get(pk=request.GET['Id']))

def delete_contact(request):
    con = modelContact()
    con.pk = request.GET['Id']
    con.delete()
    return HttpResponse()
