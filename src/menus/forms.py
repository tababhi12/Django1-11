from django import forms
from .models import Item
from restuarants.models import RestuarantLocation

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'restuarant',
            'name',
            'contents',
            'excludes',
            'public'
        ]

    def __init__(self, user = None,*args, **kwargs):
        print(user)
        super(ItemForm,self).__init__(*args, **kwargs)
        self.fields['restuarant'].queryset = RestuarantLocation.objects.filter(owner = user)#.exclude(item__isnull =False)
        