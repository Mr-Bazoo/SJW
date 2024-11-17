from django.contrib import admin
from django import forms
from .models import Blok, Leerdoel, Kind

class LeerdoelForm(forms.ModelForm):
    class Meta:
        model = Leerdoel
        fields = '__all__'
        widgets = {
            'lessen': forms.TextInput(attrs={'size': '5'}),  # Pas de grootte van het invoerveld aan
        }

class KindInline(admin.TabularInline):
    model = Leerdoel.kinderen.through  # Koppeling tussen Leerdoelen en Kinderen
    extra = 1

class LeerdoelInline(admin.TabularInline):
    model = Leerdoel
    extra = 1
    form = LeerdoelForm  # Gebruik aangepaste form voor inline

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
