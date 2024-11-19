from django.contrib import admin
from .models import Blok, Leerdoel, Kind, LeerdoelScore

class LeerdoelInline(admin.TabularInline):
    model = Leerdoel
    extra = 0  # Geen extra lege rijen
    fields = ('doel','signalering_groep', 'sleepdoel', 'automatiseringsdoelen')  # Kies de velden die je wilt tonen
    readonly_fields = ('doel',)  # Maak 'doel' alleen-lezen, indien gewenst
    show_change_link = True  # Link naar detailpagina van Leerdoel

class LeerdoelScoreInline(admin.TabularInline):
    model = LeerdoelScore
    extra = 1

@admin.register(Blok)
class BlokAdmin(admin.ModelAdmin):
    list_display = ('bloknummer', 'week', )
    inlines = [LeerdoelInline]  # Leerdoelen worden hier niet direct gekoppeld, maar via LeerdoelAdmin.

@admin.register(Kind)
class KindAdmin(admin.ModelAdmin):
    list_display = ('naam',)
    search_fields = ('naam',)
    inlines = [LeerdoelScoreInline]  # Toon leerdoelen en scores voor elk kind.

@admin.register(Leerdoel)
class LeerdoelAdmin(admin.ModelAdmin):
    list_display = ('doel', 'blok', 'sleepdoel', 'automatiseringsdoelen','signalering_groep')
    list_filter = ('sleepdoel', 'automatiseringsdoelen')
    search_fields = ('doel', 'blok', 'week', 'opmerkingen')
    inlines = [LeerdoelScoreInline]  # Toon scores van alle kinderen voor dit leerdoel.
    exclude = ('kinderen',)  # Voorkom dubbele velden door de ManyToMany-weergave te beheren via inlines
