
# -*- coding: utf-8 -*-
from django.forms import ModelForm, ModelChoiceField
from .models import CitiesData


class CitiesDataForm(ModelForm):

    class Meta:
        model = CitiesData
        fields = []

    qs = CitiesData.objects.values_list('region', flat=True).distinct()
    regions = ModelChoiceField(queryset=qs,
                               to_field_name="region",
                               empty_label=u"Выберите область")
