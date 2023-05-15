import requests
from tkinter import *
import pyperclip
import threading
import time


global waitthread

def wait_hide():
    time.sleep(3)
    l2.pack_forget()


def show():
    l3.pack()

def hide():
    l3.pack_forget()

def gefff():
    global x
    global l2
    x = e1.get()

    if (x==""):
        print("Bad Input")
        return
    words = []

    y = x.split(",")

    for word in y:
        words.append(word.strip())

    print("WORDS: " + str(len(words)))
    output = ""
    count = 0
    for word in words:
        print(count)
        url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
        response = requests.get(url)
        response_json = response.json()
        definition = (response_json[0]['meanings'][0]['definitions'][0]["definition"])
        output += word + " - " + definition + "\n"
        count += 1

    pyperclip.copy(output)
    l2 = Label(text="Result Copied To Clipboard!", font=("Fira Code", 20), fg='green',
               bg='black')
    l2.pack(pady=20)
    hide()
    waitthread.start()






def split():
    global waitthread
    waitthread = threading.Thread(target=wait_hide)
    gefy = threading.Thread(target=gefff)
    showthread = threading.Thread(target=show)
    showthread.start()
    gefy.start()


root = Tk()
root.geometry("600x300")
root.configure(bg='black')
root.resizable(False,False)
root.title("Word Parser And Definer")


title = Label(text="Word Parser And Definer", font=("Fira Code", 40), fg='green', bg='black')
title.pack()

l1 = Label(text="Enter your list of words seperated by commas below", font=("Fira Code", 10), fg='green', bg='black')
l1.pack()

e1 = Entry(font=("Fira Code", 25), fg='green', bg='black', justify='center', width='550')
e1.pack()

l3 = Label(text="Loading...", font=("Fira Code", 10), fg='green', bg='black')
l3.pack_forget()



b1 = Button(text="Submit", font=("Fira Code", 40), fg='green', bg='black', command=split)
b1.pack(side=BOTTOM, pady=20)



root.mainloop()
