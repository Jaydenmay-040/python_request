from tkinter import *
import requests
from tkinter import Tk, Message, Button
from tkinter import messagebox


def get_chuck_joke():
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random")
        data = response.json()
        return data["value"]
    except:
        messagebox.showerror("something went wrong :( ", "Please check internet connection")

window = Tk()
chuck_joke = Message(window, text=get_chuck_joke())
chuck_joke.pack()
window.geometry("200x200")


def get_new_joke():
    chuck_joke.configure(text=get_chuck_joke())

get_new_joke_btn = Button(window, text="joke", command=get_new_joke)
get_new_joke_btn.pack()

window.mainloop()


