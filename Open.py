import webbrowser
import os



def new_comand(zaprose):
    webbrowser.open(zaprose)

def internet (zaprose):
    webbrowser.open("https://yandex.ru/search/?text="+zaprose)


def VK ():
    webbrowser.open("https://vk.com/feed")


def Telegram ():
    webbrowser.open("https://web.telegram.org")


def music ():
    webbrowser.open("https://music.yandex.ru/")


def Wiki ():
    webbrowser.open("https://ru.wikipedia.org/")

def Microsoft_Office (name):
    os.startfile(f"C:/ProgramData/Microsoft/Windows/Start Menu/Programs/{name}.lnk")