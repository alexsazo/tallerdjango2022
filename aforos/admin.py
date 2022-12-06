from django.contrib import admin
from aforos.models import *

class EdificioAdmin(admin.ModelAdmin):
    pass


class EventoAdmin(admin.ModelAdmin):
    pass


class PersonaAdmin(admin.ModelAdmin):
    pass


class InscripcionAdmin(admin.ModelAdmin):
    pass

# Asociamos las clases de arriba, con los modelos que importamos de models.py
admin.site.register(Edificio, EdificioAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Inscripcion, InscripcionAdmin)