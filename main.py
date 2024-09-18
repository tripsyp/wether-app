from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(city):
    api_key = '7bcf22c885474710b0f83144242308'
    base_url = 'http://api.weatherapi.com/v1/current.json?'
    complete_url = f"{base_url}key={api_key}&q={city}&aqi=no"

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        main = data['current']
        weather_info = {
            'city': data['location']['name'],
            'temp': main['temp_c'],
            'description': main['condition']['text'],
            'humidity': main['humidity'],
            'pressure': main['pressure_mb'],
        }
        return weather_info
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_info = None
    if request.method == 'POST':
        city = request.form['city']
        weather_info = get_weather(city)
    return render_template('index.html', weather_info=weather_info)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
