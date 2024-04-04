import datetime

import requests
from aiogram import types, F
from aiogram.filters import Command

from Keyboards.Reply.LocationKeyboard import location_keyboard
from config import WEATHER_API_KEY
from loader import dp

params = {
    "lat": '',
    "lon": '',
    "appid": WEATHER_API_KEY,
    "lang": "ua",
    "units": "metric"
}


@dp.message(Command('weather'))
async def process_start_command(message: types.Message):
    await message.answer("Надішли гео, щоб дізнатися погоду", parse_mode='HTML', reply_markup=location_keyboard())


@dp.message(F.location)
async def location_handler(message: types.Message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    weather = get_weather(latitude, longitude)
    await message.answer(f"{weather}", parse_mode='HTML')


def get_weather(latitude, longitude):
    params['lat'] = str(latitude)
    params['lon'] = str(longitude)
    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    result = response.json()
    name = result['name']
    temperature = str(result['main']['temp'])
    temperature_min = str(result['main']['temp_min'])
    temperature_max = str(result['main']['temp_max'])
    weather_description = str(result['weather'][0]['description'])
    wind_speed = str(result['wind']['speed'])
    try:
        rain = str(result['rain']['1h'])
    except KeyError:
        rain = '0'
    sunrise_obj = datetime.datetime.fromtimestamp(result['sys']['sunrise'])
    sunset_obj = datetime.datetime.fromtimestamp(result['sys']['sunset'])
    sunrise = str(sunrise_obj.time())
    sunset = str(sunset_obj.time())

    weather = ("✳️ " + name + " ✳️" +
               "\n▫️ Температура - " + temperature + " °C" +
               "\n(" + temperature_min + " °C min, " + temperature_max + " °C max)" +
               "\n▫️ Опис - " + weather_description +
               "\n▫️ Швидкість вітру - " + wind_speed + " м/c" +
               "\n▫️ Дощ - " + rain +
               "\n▫️ Світанок - " + sunrise +
               "\n▫️ Захід - " + sunset)

    print("User link - " + response.url)
    return weather
