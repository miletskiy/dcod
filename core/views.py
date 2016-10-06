
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
# Create your views here.
from .forms import CitiesDataForm
from .models import CitiesData


def index(request):
    form = CitiesDataForm()
    if request.GET.get('regions'):
        form = CitiesDataForm(request.GET)
    form.fields['regions'].widget.attrs = {'class': 'form-control'}
    context = {'form': form, 'data': {}}

    if form.is_valid():
        selected_region = form.cleaned_data['regions']
        qs = CitiesData.objects.filter(region=selected_region)
        data = serializers.serialize('json', qs)
        context.update({'data': data, 'region': selected_region})

    return render(request, 'core.html', context)
