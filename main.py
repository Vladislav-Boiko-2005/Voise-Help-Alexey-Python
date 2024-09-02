import json, pyaudio
import pyttsx3
from pyaudio import*
from vosk import Model, KaldiRecognizer
import speech_recognition as sr
import function   # подключение функций помощника
import Open
import dialog_windows


def ReadVoise():
    r=sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("идет запись голоса")
        audio=r.listen(source)
        try:
            querty=r.recognize_google(audio, language="ru-RU")
            return str(querty.lower()). capitalize()
        except :
            return "ошибка \nповторите команду"





#озвучка текста ботом
def TextVoise(text):
    # Создаем экземпляр движка pyttsx3
    engine = pyttsx3.init()
    # Настраиваем голос на русский
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    # Озвучиваем текст
    engine.say(str(text))
    engine.runAndWait()


def NewComand(comand):
    file=open("new_comand.txt","r",encoding="utf-8")
    strings=file.readlines()
    for i in strings:
        stroc1=""
        stroc2=""
        flag=1
        for j in i:
            if j != "$" and flag:
                stroc1+=j
            else:
                if flag==0:
                    stroc2+=j
                flag = 0
        if stroc1==comand:
            Open.new_comand(stroc2)
            return 1
    return 0


def TextVoiseTXT(namefile):
    # Создаем экземпляр движка pyttsx3
    engine = pyttsx3.init()
    # Настраиваем голос на русский
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    file = open(namefile, "r", encoding="utf-8")
    strings=file.readlines()
    for vivod in strings:
        engine.say(vivod)
        engine.runAndWait()
    file.close()



def TextFormat(text):
    text=text.lower()
    text=text.replace("алексей","")
    if len(text)>0:
        while text[0]==" ":
            text=text[1:]
        while text[-1]==" ":
            text=text[:-1]
        return text
    return ""

TextVoiseTXT("hello.txt")

# обработка всех запросов
while True:
    zapros =ReadVoise()
    print(zapros)
    if zapros.count("Алексей")>0 or zapros.count("алексей")>0:
        zapros=TextFormat(zapros)
        print(zapros)
        if zapros.count("скажи какая погода")>0:
            TextVoise("скажите в каком городе вы хотите узнать погоду")
            city = TextFormat(ReadVoise())
            TextVoise(function.weather_to_city(city))
            continue
        if zapros.count("что ты умеешь")>0:
            TextVoiseTXT("answers.txt")
            continue
        if zapros.count("включи музыку")>0:
            Open.music()
            TextVoise("открываю яндекс музыку")
            continue
        if zapros.count("открой википедию")>0:
            Open.Wiki()
            TextVoise("открываю сайт википедия")
            continue
        if zapros.count("открой вконтакте")>0:
            Open.VK()
            TextVoise("открываю вашу страницу вконтакте")
            continue
        if zapros.count("открой telegram")>0:
            Open.Telegram()
            TextVoise("открываю телеграм веб")
            continue
        if zapros.count("открой word")>0:
            Open.Microsoft_Office("Word")
            TextVoise("открываю word")
            continue
        if zapros.count("открой excel")>0:
            Open.Microsoft_Office("Excel")
            TextVoise("открываю exsel")
            continue
        if zapros.count("открой powerpoint")>0:
            Open.Microsoft_Office("PowerPoint")
            TextVoise("открываю PowerPoint")
            continue
        if zapros.count("открой access")>0:
            Open.Microsoft_Office("Access")
            TextVoise("открываю access")
            continue
        if zapros.count("найди в интернете")>0:
            Open.internet(zapros.replace("найди в интернете",""))
            TextVoise("открываю ваш браузер")
            continue
        if (NewComand(zapros)):
            print("исполняю команду пользователя")
            TextVoise("исполняю команду пользователя")
            continue
        if zapros.count("сделай новую команду"):
            TextVoise("Создайте новую команду")
            dialog_windows.CreatNewComand()