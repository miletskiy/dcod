from __future__ import unicode_literals

from django.db import models


class CitiesData(models.Model):

    class Meta:
        verbose_name = "CitiesData"
        verbose_name_plural = "CitiesDatas"

    name = models.CharField(
        max_length=255,
        verbose_name=u'Name of the city')

    region = models.CharField(
        max_length=255,
        verbose_name=u'Region of the city')

    data = models.IntegerField(
        verbose_name=u'Data for the city'
    )

    def __unicode__(self):
        return u'{} {}'.format(self.name, self.region)
