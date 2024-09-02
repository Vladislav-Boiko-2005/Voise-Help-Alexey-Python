# прогноз погоды
import requests
from transliterate import translit
import json



def weather_to_city (city):
    # указываем город на русском с заглавной буквы
    city=translit(city, 'ru')   #проверка и перевод текста на русские буквы
    city=city.capitalize () # Форматирование текста
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    # отправляем запрос на сервер и сразу получаем результат
    print(city)
    weather_data = requests.get(url).json()
    try:
        weather = weather_data["weather"][0]["description"]#пасмурно или ясно
        temperature = round(weather_data['main']['temp'])
        temperature_feels = round(weather_data['main']['feels_like'])
        # выводим значения на экран
        return (f"Сейчас в городе {city} по цельсию {str(temperature)}  \n{weather} \n")          #Ощущается как {str(temperature_feels)} ")
    except:
        return "Простите произошла ошибка и я не могу ответить\n если хотите узнать погоду то попробуйте повторить свой запрос"






