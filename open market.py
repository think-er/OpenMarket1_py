from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk

# 왜 GUI에 클래스가 필요한걸까?

LOGO_WIDTH = 100
LOGO_HEIGHT = 100
LOGO_X = 140
LOGO_Y = 50

LOGIN_WIDTH = 20
LOGIN_HEIGHT = 20
LOIGN_ENTRY_WIDTH = 150
LOIGN_ENTRY_HEIGHT = 30
LOGIN_X = 100
LOGIN_Y = 260

win = Tk()
win.title("Login")
win.geometry("400x400")
win.configure(bg="white")
win.resizable(width=FALSE, height=FALSE)

logo_img = Image.open('img/login/logo.png').resize((LOGO_WIDTH, LOGO_HEIGHT))
logo_img = ImageTk.PhotoImage(logo_img)
logo_label = Label(win, image=logo_img, bg="white")
logo_label.place(x=LOGO_X,y=LOGO_Y)

title_font = Font(
    family='Calibri Light',
    size=20
)

input_login_font = Font(
    family='Consolas',
    weight='bold',
    size=10
)

title_label = Label(win, text="Open Market", font=title_font, bg="white")
title_label.place(x=LOGO_X-12,y=LOGO_Y+130)

id_img = Image.open('img/login/id.png').resize((LOGIN_WIDTH, LOGIN_HEIGHT))
id_img = ImageTk.PhotoImage(id_img)
id_label = Label(win, image=id_img, bg="white")
id_label.place(x=LOGIN_X,y=LOGIN_Y)
id_entry = Entry(win, font=input_login_font, relief="solid")
id_entry.place(x=LOGIN_X+30,y=LOGIN_Y,width=LOIGN_ENTRY_WIDTH,height=LOIGN_ENTRY_HEIGHT)


password_img = Image.open('img/login/password.png').resize((LOGIN_WIDTH, LOGIN_HEIGHT))
password_img = ImageTk.PhotoImage(password_img)
password_label = Label(win, image=password_img, bg="white")
password_label.place(x=LOGIN_X,y=LOGIN_Y+30)
password_entry = Entry(win, show="*", font=input_login_font, relief="solid")
password_entry.place(x=LOGIN_X+30,y=LOGIN_Y+30,width=LOIGN_ENTRY_WIDTH,height=LOIGN_ENTRY_HEIGHT)


win.mainloop()