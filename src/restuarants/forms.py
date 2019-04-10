from django import forms
from .models import RestuarantLocation
from .validators import validate_category

class RestuarantCreateForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField(required=False)
    category = forms.CharField(required=False)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'Hello':
            raise forms.ValidationError('Not a valid Name')


class RestuarantLocationCreateForm(forms.ModelForm):
    #category = forms.CharField(required = False,validators = [validate_category])
    class Meta:
        model = RestuarantLocation
        fields = [
            'name',
            'location',
            'category',
        ]
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'Hello':
            raise forms.ValidationError('Not a valid Name')
        return name
    
        