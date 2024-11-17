from django.db import models

class Blok_week(models.Model):
    blok = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Blok_week"

class Lessen(models.Model):
    les = models.CharField(max_length=2)  # Opslag voor lessen, bijvoorbeeld 'W1' of 'G2'
    les_blok = models.ManyToManyField(Blok_week, related_name='lessen')

    class Meta:
        verbose_name_plural = "Lessen"

class MyInteger(models.Model):
    my_model = models.ForeignKey(Lessen, on_delete=models.CASCADE, related_name='numbers')
    value = models.IntegerField()  # Opslag voor een geheel getal gekoppeld aan een les

    class Meta:
        verbose_name_plural = "MyInteger"

class Kind(models.Model):
    naam = models.CharField(max_length=25)  # Opslag voor namen van kinderen
    kind_blok = models.ManyToManyField(Blok_week, related_name='kinderen')

    class Meta:
        verbose_name_plural = "Kind"

class Doelen(models.Model):
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)
    leerdoel = models.CharField(max_length=50)  # Opslag voor specifieke leerdoelen voor een kind
    doel_blok = models.ManyToManyField(Blok_week, related_name='doelen')

    class Meta:
        verbose_name_plural = "Doelen"

class MomentVanVereisteBeheersing(models.Model):
    moment = models.CharField(max_length=50)  # Beschrijft een tijdsperiode waarin beheersing vereist is
    moment_blok = models.ManyToManyField(Blok_week, related_name='momenten')

    class Meta:
        verbose_name_plural = "MomentVanVereisteBeheersing"

class Voorkennis(models.Model):
    voorkennis = models.CharField(max_length=50)  # Opslag voor benodigde voorkennis
    kennis_blok = models.ManyToManyField(Blok_week, related_name='voorkennis')

    class Meta:
        verbose_name_plural = "Voorkennis"

class SignaleringGroep(models.Model):
    doel = models.ForeignKey(Doelen, on_delete=models.CASCADE)
    signalering = models.CharField(max_length=50)  # Signaleringsinformatie gekoppeld aan een doel
    signalering_blok = models.ManyToManyField(Blok_week, related_name='signaleringen')

    class Meta:
        verbose_name_plural = "SignaleringGroep"

class Opmerkingen(models.Model):
    opmerking = models.CharField(max_length=150)  # Opslag voor extra opmerkingen
    opmerking_blok = models.ManyToManyField(Blok_week, related_name='opmerkingen')

    class Meta:
        verbose_name_plural = "Opmerkingen"

class Behaaldstatus(models.Model):
    sleepdoel = models.BooleanField(default=False)  # Boolean veld om aan te geven of een doel een sleepdoel is
    automatiseringsdoelen = models.BooleanField(default=False)  # Boolean veld voor automatiseringsdoelen
    status_blok = models.ManyToManyField(Blok_week, related_name='behaaldstatussen')

    class Meta:
        verbose_name_plural = "Behaaldstatus"
