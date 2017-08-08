# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from reports.models import Station, Report, Incident

from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from django.core import urlresolvers

class IncidentAdmin(admin.ModelAdmin):
    list_display = ('case', 'bpd_id', 'title', 'incident_dt', 'location',
                    'station', 'location_id', 'body', 'icon', 'published_at',
                    'updated_at', 'arrested', 'prohibition_order', 'warrant',
                    'parsed_time', 'parsed_case')
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows':10, 'cols':80})},
    }

class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'city')
    ordering = ('abbreviation',)

class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_dt', 'incidents_count', 'email_id', 'processed', 'created_dt')

admin.site.register(Incident, IncidentAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(Report, ReportAdmin)
