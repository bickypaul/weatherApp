# weatherApp
A basic django based weather App.
Weather Api endpoint used: www.openweathermap.org

It is a django based web app which shows the information about the weather of a particular city.
A user can add and delete a city on the browser. 

This is just a practice projects. Do check out the source codes.

## Requirements (tested on)
1. Ubuntu 18.04
2. Virtual Environment
3. Django 2.1.2
4. pip install requests
5. sign up to www.openweathermap.org and get the API key.

## To execute
1. git clone https://github.com/bickypaul/weatherApp
2. Activate the virtual environment for example: $ source env/bin/activate
3. cd weatherApp
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py createsuperuser (to add data through django admin)
7. python manage.py runserver
8. Go to http://localhost:8000

### Note: Make sure you integrate your API key in views.py file which can obtained from the www.openweathermap.org after you sign up. I have used the free trial.

Next you can add city and delete city and see the weather information of a city. For example: City Name, Temperature, Description, Icon.

Thanks.
