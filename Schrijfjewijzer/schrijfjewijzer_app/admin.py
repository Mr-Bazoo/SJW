from django.contrib import admin
from .models import Blok, Leerdoel, Kind

class KindInline(admin.TabularInline):
    model = Leerdoel.kinderen.through  # Koppeling tussen Leerdoelen en Kinderen
    extra = 1

class LeerdoelInline(admin.TabularInline):
    model = Leerdoel
    extra = 1
    fields = ('doel', 'lessen', 'voorkennis', 'opmerkingen', 'sleepdoel', 'automatiseringsdoelen')

@admin.register(Blok)
class BlokAdmin(admin.ModelAdmin):
    list_display = ('bloknummer', 'week')
    inlines = [LeerdoelInline]

@admin.register(Kind)
class KindAdmin(admin.ModelAdmin):
    list_display = ('naam',)
    search_fields = ('naam',)
    inlines = [KindInline]  # Hiermee zie je bij welk leerdoel elk kind hoort

    def get_queryset(self, request):
        """Zorgt ervoor dat gerelateerde doelen zichtbaar zijn in de queryset."""
        qs = super().get_queryset(request)
        return qs.prefetch_related('leerdoelen')  # Optimaliseert de query

@admin.register(Leerdoel)
class LeerdoelAdmin(admin.ModelAdmin):
    list_display = ('doel', 'blok', 'sleepdoel', 'automatiseringsdoelen')
    list_filter = ('sleepdoel', 'automatiseringsdoelen')
    search_fields = ('doel', 'voorkennis', 'opmerkingen')
    inlines = [KindInline]  # Toon ook in Leerdoel de kinderen
    exclude = ('kinderen',)  # Voorkom dubbele weergave van kinderen in standaardvelden
