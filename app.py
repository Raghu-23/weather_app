from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '016c4cf27e9d2bd96c2d3ddf14e847de'  # Replace with your OpenWeatherMap API key

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
    'city': city.title(),
    'temperature': data['main']['temp'],
    'description': data['weather'][0]['description'].title(),
    'humidity': data['main']['humidity'],
    'wind': data['wind']['speed'],
    'country': data['sys']['country'],
    'icon': data['weather'][0]['icon']  # NEW
}

        else:
            weather = 'error'
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
