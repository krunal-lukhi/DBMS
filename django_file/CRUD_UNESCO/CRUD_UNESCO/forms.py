#forms.py
from django import forms
from CRUD_UNESCO.models import InstModel
from CRUD_UNESCO.models import SiteModel
from CRUD_UNESCO.models import CountryModel

class InstForms(forms.ModelForm):
    class Meta: 
        model=InstModel
        fields="__all__"

class SiteForms(forms.ModelForm):
    class Meta: 
        model=SiteModel
        fields="__all__"

class CountryForms(forms.ModelForm):
    class Meta: 
        model=CountryModel
        fields="__all__"

