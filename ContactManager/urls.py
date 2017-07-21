"""
Definition of urls for ContactManager.
"""

from datetime import datetime
from django.conf.urls import patterns, url

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.contact_manager', name='contact_manager'),
    url(r'^contacts$', 'app.views.all_contacts', name='all_contacts'),
    url(r'^insert$', 'app.views.insert_contact', name='insert_contact'),
    url(r'^update$', 'app.views.update_contact', name='update_contact'),
    url(r'^delete$', 'app.views.delete_contact', name='delete_contact')
)
