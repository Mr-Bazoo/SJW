from django.contrib import admin
from .models import (
    Blok_week,Lessen, MyInteger, Kind, Doelen, 
    MomentVanVereisteBeheersing, Voorkennis, 
    SignaleringGroep, Opmerkingen, Behaaldstatus
)

# Registreer alle modellen met hun aangepaste ModelAdmin
admin.site.register(Blok_week)
admin.site.register(Lessen)
admin.site.register(MyInteger)
admin.site.register(Kind)
admin.site.register(Doelen)
admin.site.register(MomentVanVereisteBeheersing)
admin.site.register(Voorkennis)
admin.site.register(SignaleringGroep)
admin.site.register(Opmerkingen)
admin.site.register(Behaaldstatus)