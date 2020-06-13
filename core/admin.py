from django.contrib import admin
from core.models import Evento

class EventoAdmin(admin.ModelAdmin):
  list_display = ('titulo','usuario', 'data_evento', 'data_criacao', 'local')
  list_filter = ('titulo','data_evento','local',)

admin.site.register(Evento, EventoAdmin)