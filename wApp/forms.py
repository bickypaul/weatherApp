from django.forms import ModelForm, TextInput
from .models import City

# using the modelform class to map with the database model, 
# saves lot of code in the code as well as in the template.
class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'City Name'})}
