This is a small Python/Flask app that will retrieve weather information.  It uses a free API from https://openweathermap.org/api. You'll need to obtain a key from OpenWeatherMap.

Pre-requisite:
Python3 and pip must be installed on your computer.
Make a folder called MyWeatherApp (or whatever you want to name the app)
Clone the files to this folder.
Then run:  pip install -r requirements.txt
Create a .env file with the weather key obtained from OpenWeatherApp
ex:
export WEATHER_KEY='xxxxxxxxxxxxxxxxxxxxxxxxxxxx'

To run locally you'll need to:

cd into /MyWeatherApp folder
export FLASK_APP=main.py
flask run

This will let you run on your localhost on port 5000

