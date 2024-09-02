import tkinter as tk
from tkinter import simpledialog


def CreatNewComand():
    root = tk.Tk()
    root.withdraw() # Скрываем главное окно

    # Создаем диалоговое окно с двумя строками для ввода
    text1 = simpledialog.askstring("ввод названия команды", "Введите команду после которой алексей будет открывать страницу в интернете например (Алексей открой банкинг):")
    text2 = simpledialog.askstring("ввод адреса сайта", "Введите адресс страницы например (https://bank.org) вы можете взять его из строки вверху браузера:")
    text1=text1.lower()
    text1=text1.replace("алексей","")
    if len(text1)>0:
        while(text1[0]==" "):
            text1=text1[1:]
        while(text1[-1]==" "):
            text1=text1[:-1]
    file=open("new_comand.txt","w",encoding="utf-8")
    file.write(f"\n{text1}${text2}")
    file.close()
    return 1