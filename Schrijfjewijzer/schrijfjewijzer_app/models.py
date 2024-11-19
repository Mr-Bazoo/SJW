from django.db import models

KEUZES = (
    (2, "x"),
    (1, "~"),
    (0, "v"),
)

class Kind(models.Model):
    naam = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Kinderen"

    def __str__(self):
        return self.naam


class Blok(models.Model):
    bloknummer = models.PositiveSmallIntegerField()
    week = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = "Blokken"

    def __str__(self):
        return f"Blok {self.bloknummer} - Week {self.week}"


class Leerdoel(models.Model):
    blok = models.ForeignKey('Blok', related_name='leerdoelen', on_delete=models.CASCADE)
    doel = models.CharField(max_length=50)
    kinderen = models.ManyToManyField('Kind', related_name='leerdoelen')
    lessen = models.CharField(max_length=10, blank=True, null=True)
    voorkennis = models.CharField(max_length=50, blank=True, null=True)
    opmerkingen = models.CharField(max_length=150, blank=True, null=True)
    signalering_groep = models.CharField(max_length=150, blank=True, null=True)
    sleepdoel = models.BooleanField(default=False)
    automatiseringsdoelen = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Leerdoelen"

    def __str__(self):
        return self.doel


class LeerdoelScore(models.Model):
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE, related_name='scores')
    leerdoel = models.ForeignKey(Leerdoel, on_delete=models.CASCADE, related_name='scores')
    keuze1 = models.IntegerField(choices=KEUZES, default=0)
    keuze2 = models.IntegerField(choices=KEUZES, default=0)
    keuze3 = models.IntegerField(choices=KEUZES, default=0)

    class Meta:
        verbose_name_plural = "Leerdoel Scores"
        unique_together = ('kind', 'leerdoel')

    def __str__(self):
        return f"{self.kind} - {self.leerdoel}"
