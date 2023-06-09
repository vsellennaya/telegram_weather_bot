import requests
import datetime
from config import weather_tbot

def get_weather(city, weather_tbot):

    code_to_smile = {
        'Clear': 'Ясно \U0001F324',
        'Clouds': 'Облачно \U000026C5',
        'Rain': 'Дождь \U00002614',
        'Drizzle': 'Дождь \U0001F327',
        'Thunderstorm': 'Гроза \U000026C8',
        'Snow': 'Снег \U0001F328',
        'Mist': 'Туман \U0001F32B'
    }

    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_tbot}&units=metric'
        )
        data = r.json()
        #pprint(data)

        city = data['name']
        cur_weather = data['main']['temp']

        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Look outside, cannot get what is there!'

        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
              f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
              f"Хорошего дня!"
              )

    except Exception as ex:
        print(ex)
        print('Check the name of the city')

def main():
    city = input('Enter the city name: ')
    get_weather(city, weather_tbot)

if __name__=='__main__':
    main()


