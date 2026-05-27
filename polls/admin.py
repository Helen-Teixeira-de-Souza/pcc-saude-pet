from django.contrib import admin
from .models import Pet, Vacina, Consulta, Tutor, HistoricoPeso

admin.site.register(Pet)
admin.site.register(Vacina)
admin.site.register(Consulta)
admin.site.register(HistoricoPeso)
admin.site.register(Tutor)