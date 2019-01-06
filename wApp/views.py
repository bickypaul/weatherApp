import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm

def index(request):
    # this is the api endpoint to get the weather information, sign up in www.openweathermap.org
    url = 'https://api.openweathermap.org/data/2.5/find?q={}&units=imperial&appid=YOUR_API_KEY'

    '''
    This is the main part of the project where a request method is checked, if the request method is POST
    the user will be able to add a city to the database. 
    The cities that are already in the database will be rendered on the browser otherwise.
    Information such as, city name, temperature(in F), description and icon will show up on the browser.
    '''
    
    # adding a new city in the database.
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    # if not post method, simply intitaiting an empty form on the browser.
    form = CityForm() 
    
    # quering all the cities from the database
    cities = City.objects.all()
    weather_data = []


    # appending the weather characteristics (python dictionary) along with their informations(mentioned above) in a list.
    for city in cities:
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city_id': city.id,
            'city': city.name,
            'temperature': r['list'][0]['main']['temp'],
            'description': r['list'][0]['weather'][0]['description'],
            'icon': r['list'][0]['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    # the context that is sent passed to the template that is going to get rendered.
    context = {
        'weather_data': weather_data,
        'form': form,
    }

    return render(request, 'wApp/weather.html', context)

# deleting a particular city.
def deleteCity(request, city_id):
    City.objects.get(pk=city_id).delete()

    return redirect('index')

#deleting all the cities.
def deleteAll(request):
    City.objects.all().delete()

    return redirect('index')





