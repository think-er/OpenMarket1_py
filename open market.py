from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
import pandas as pd

# 왜 GUI에 클래스가 필요한걸까?

# logo image+title
LOGO_WIDTH = 100
LOGO_HEIGHT = 100
LOGO_X = 150
LOGO_Y = 30

# id/password image+Entry
LOGIN_WIDTH = 20
LOGIN_HEIGHT = 20
LOIGN_ENTRY_WIDTH = 150
LOIGN_ENTRY_HEIGHT = 30
LOGIN_X = 100
LOGIN_Y = 230

# found id/password/register button
OPTIONS_X = 70
OPTIONS_Y = 350

win = Tk()
win.title("Login")
win.geometry("400x400")
# 배경화면을 하얀색으로
win.configure(bg="white")
win.resizable(width=FALSE, height=FALSE)

logo_img = Image.open('img/login/logo.png').resize((LOGO_WIDTH, LOGO_HEIGHT))
logo_img = ImageTk.PhotoImage(logo_img)
logo_label = Label(win)
logo_label.config(image=logo_img, bg="white")
logo_label.place(x=LOGO_X,y=LOGO_Y)

title_font = Font(
    family='Tahoma',
    size=20
)

title_label = Label(win)
title_label.config(text="Open Market", font=title_font, bg="white", foreground='orange')
title_label.place(x=LOGO_X-20,y=LOGO_Y+130)

input_login_font = Font(
    family='Consolas',
    weight='bold',
    size=10
)

id_img = Image.open('img/login/id.png').resize((LOGIN_WIDTH, LOGIN_HEIGHT))
id_img = ImageTk.PhotoImage(id_img)
id_label = Label(win)
id_label.config(image=id_img, bg="white")
id_label.place(x=LOGIN_X,y=LOGIN_Y)
id_entry = Entry(win)
id_entry.config(font=input_login_font, relief="groove")
id_entry.place(x=LOGIN_X+30,y=LOGIN_Y,width=LOIGN_ENTRY_WIDTH,height=LOIGN_ENTRY_HEIGHT)

password_img = Image.open('img/login/password.png').resize((LOGIN_WIDTH, LOGIN_HEIGHT))
password_img = ImageTk.PhotoImage(password_img)
password_label = Label(win)
password_label.config(image=password_img, bg="white")
password_label.place(x=LOGIN_X,y=LOGIN_Y+30)
password_entry = Entry(win)
password_entry.config(show="*", font=input_login_font, relief="groove")
password_entry.place(x=LOGIN_X+30,y=LOGIN_Y+30,width=LOIGN_ENTRY_WIDTH,height=LOIGN_ENTRY_HEIGHT)

def login_user():
    df_user = pd.read_csv('csv/user.csv')
    df_user.set_index(df_user['USER_ID'], inplace=True)
    id = id_entry.get()
    pw = password_entry.get()

    # 아이디, 비밀번호 입력 확인
    if id == "":
        print("아이디를 입력해 주세요.")
        return 0
    else:
        if pw == "":
            print("비밀번호를 입력해 주세요.")
            return 0

    if id in df_user.index:
        id_check = True
        if df_user.loc[id, 'USER_PW'] == pw:
            pw_check = True
        else:
            pw_check = False
    else:
        id_check = False

    if id_check == True and pw_check == True:
        print("로그인 성공")
    else:
        print("아이디(로그인 전용 아이디) 또는 비밀번호를 잘못 입력했습니다.\n입력하신 내용을 다시 확인해주세요.")

def find_password():
    df_user = pd.read_csv('csv/user.csv', index_col=0)

def find_id():
    df_user = pd.read_csv('csv/user.csv', index_col=0)

def register_user():
    df_user = pd.read_csv('csv/user.csv', index_col=0)




login_btn = Button(win)
login_btn.config(text="로그인", relief="flat", bg="orange", foreground='white', command=login_user)
login_btn.place(x=LOGIN_X+30,y=LOGIN_Y+70,width=150,height=30)

password_find_btn = Button(win)
password_find_btn.config(text="비밀번호 찾기", relief="flat", bg="white")
password_find_btn.place(x=OPTIONS_X,y=OPTIONS_Y)

id_find_btn = Button(win)
id_find_btn.config(text="아이디 찾기", relief="flat", bg="white")
id_find_btn.place(x=OPTIONS_X+100,y=OPTIONS_Y)

user_register_btn = Button(win)
user_register_btn.config(text="회원 가입", relief="flat", bg="white")
user_register_btn.place(x=OPTIONS_X+200,y=OPTIONS_Y)

win.mainloop()
