from django import forms

class RestuarantCreateForm(forms.Form):
    name = forms.CharField(max_length=120)
    location = forms.CharField(required=False)
    category = forms.CharField(required=False)