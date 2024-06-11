# admin.py en la aplicación 'aulas'
from django.contrib import admin
from .models import Aula, Notificacion

@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'aula', 'preferencia')
    list_filter = ('preferencia',)
    search_fields = ('usuario__username', 'aula__nombre')