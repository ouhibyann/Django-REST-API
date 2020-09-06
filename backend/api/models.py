from django.db import models


class Tower(models.Model):

    class Meta:
        managed = False
        db_table = 'Tower'

    index = models.BigIntegerField(blank=True, null=True)
    radio = models.TextField(blank=True, null=True)
    mcc = models.BigIntegerField(blank=True, null=True)
    net = models.BigIntegerField(blank=True, null=True)
    area = models.BigIntegerField(blank=True, null=True)
    cell = models.BigIntegerField(blank=True, primary_key=True)
    unit = models.BigIntegerField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    range = models.BigIntegerField(blank=True, null=True)
    samples = models.BigIntegerField(blank=True, null=True)
    changeable = models.BigIntegerField(blank=True, null=True)
    created = models.BigIntegerField(blank=True, null=True)
    updated = models.BigIntegerField(blank=True, null=True)
    averagesignal = models.BigIntegerField(db_column='averageSignal', blank=True, null=True)


