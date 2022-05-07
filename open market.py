from tkinter import *
from tkinter.font import Font
from tkinter.ttk import Combobox
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
LOGIN_ENTRY_WIDTH = 150
LOGIN_ENTRY_HEIGHT = 30
LOGIN_X = 100
LOGIN_Y = 210

# found id/password/register button
OPTIONS_X = 70
OPTIONS_Y = 350

# register user label+entry+combobox+button
# birth/gender/phone
REGISTER_X = 100
REGISTER_Y = 20
REGISTER_ENTRY_WIDTH = 200
REGISTER_ENTRY_HEIGHT = 25
REGISTER_BIRTH_WIDTH = 64
REGISTER_GENDER_HEIGHT = 30
REGISTER_PHONE_WIDTH = 140
REGISTER_PHONE_CHECK_X = 244
REGISTER_PHONE_CHECK_WIDTH = 56

win = Tk()
win.title("로그인")
win.geometry("400x400")

default_font = Font(
    family="TkDefaultFont",
    size=10
)

win.option_add("*Font", default_font)
win.resizable(width=FALSE, height=FALSE)

logo_img = Image.open('img/logo.png').resize((LOGO_WIDTH, LOGO_HEIGHT))
logo_img = ImageTk.PhotoImage(logo_img)
logo_label = Label(win)
logo_label.config(image=logo_img)
logo_label.place(x=LOGO_X,y=LOGO_Y)

title_font = Font(
    family='Impact',
    size=20
)

title_label = Label(win)
title_label.config(text="Open Market",font=title_font,foreground='orange')
title_label.place(x=LOGO_X-20,y=LOGO_Y+120)

id_img = Image.open('img/id.png').resize((LOGIN_WIDTH, LOGIN_HEIGHT))
id_img = ImageTk.PhotoImage(id_img)
id_label = Label(win)
id_label.config(image=id_img)
id_label.place(x=LOGIN_X,y=LOGIN_Y)
id_entry = Entry(win)
id_entry.config(relief="groove")
id_entry.place(x=LOGIN_X+30,y=LOGIN_Y,width=LOGIN_ENTRY_WIDTH,height=LOGIN_ENTRY_HEIGHT)

password_img = Image.open('img/password.png').resize((LOGIN_WIDTH, LOGIN_HEIGHT))
password_img = ImageTk.PhotoImage(password_img)
password_label = Label(win)
password_label.config(image=password_img)
password_label.place(x=LOGIN_X,y=LOGIN_Y+30)
password_entry = Entry(win)
password_entry.config(show="*",relief="groove")
password_entry.place(x=LOGIN_X+30,y=LOGIN_Y+30,width=LOGIN_ENTRY_WIDTH,height=LOGIN_ENTRY_HEIGHT)

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
    df_user = pd.read_csv('csv/user.csv')
    df_user.set_index(df_user['USER_ID'], inplace=True)

def find_id():
    df_user = pd.read_csv('csv/user.csv')
    df_user.set_index(df_user['USER_ID'], inplace=True)

def register_user():
    win.geometry("400x600")
    win.title("회원가입")
    frame = Frame(win)
    frame.place(width=400, height=600)
    df_user = pd.read_csv('csv/user.csv')
    df_user.set_index(df_user['USER_ID'], inplace=True)

    id_label = Label(frame)
    id_label.config(text="아이디")
    id_label.place(x=REGISTER_X,y=REGISTER_Y)

    id_entry = Entry(frame)
    id_entry.config(relief="groove")
    id_entry.place(x=REGISTER_X,y=REGISTER_Y+20,width=REGISTER_ENTRY_WIDTH,height=REGISTER_ENTRY_HEIGHT)

    password_label2 = Label(frame)
    password_label2.config(text="비밀번호")
    password_label2.place(x=REGISTER_X,y=REGISTER_Y+70)

    password_entry = Entry(frame)
    password_entry.config(show='*',relief="groove")
    password_entry.place(x=REGISTER_X,y=REGISTER_Y+90,width=REGISTER_ENTRY_WIDTH,height=REGISTER_ENTRY_HEIGHT)

    password_reconfirm_label = Label(frame)
    password_reconfirm_label.config(text="비밀번호 재확인")
    password_reconfirm_label.place(x=REGISTER_X,y=REGISTER_Y+140)

    password_reconfirm_label = Entry(frame)
    password_reconfirm_label.config(show='*',relief="groove")
    password_reconfirm_label.place(x=REGISTER_X,y=REGISTER_Y+160,width=REGISTER_ENTRY_WIDTH,height=REGISTER_ENTRY_HEIGHT)

    name_label = Label(frame)
    name_label.config(text="이름")
    name_label.place(x=REGISTER_X,y=REGISTER_Y+210)

    name_entry = Entry(frame)
    name_entry.config(relief="groove")
    name_entry.place(x=REGISTER_X,y=REGISTER_Y+230,width=REGISTER_ENTRY_WIDTH,height=REGISTER_ENTRY_HEIGHT)

    birth_label = Label(frame)
    birth_label.config(text="생년월일")
    birth_label.place(x=REGISTER_X,y=REGISTER_Y+280)

    birth_year_entry = Entry(frame)
    birth_year_entry.config(relief="groove")
    birth_year_entry.place(x=REGISTER_X,y=REGISTER_Y+300,width=REGISTER_BIRTH_WIDTH,height=REGISTER_ENTRY_HEIGHT)

    birth_month_combo = Combobox(frame)
    birth_month_combo.config(values=["월", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], state="readonly")
    birth_month_combo.current(0)
    birth_month_combo.place(x=REGISTER_X+68,y=REGISTER_Y+300,width=REGISTER_BIRTH_WIDTH,height=REGISTER_ENTRY_HEIGHT)

    birth_day_entry = Entry(frame)
    birth_day_entry.config(relief="groove")  
    birth_day_entry.place(x=REGISTER_X+136,y=REGISTER_Y+300,width=REGISTER_BIRTH_WIDTH,height=REGISTER_ENTRY_HEIGHT)

    gender_label = Label(frame)
    gender_label.config(text="성별")
    gender_label.place(x=100,y=REGISTER_Y+350)
    gender_combo = Combobox(frame)
    gender_combo.config(values=["성별", "남자", "여자", "선택 안함"], state="readonly")
    gender_combo.current(0)
    gender_combo.place(x=REGISTER_X,y=REGISTER_Y+370,width=REGISTER_ENTRY_WIDTH,height=REGISTER_GENDER_HEIGHT)

    phone_label = Label(frame)
    phone_label.config(text="휴대전화")
    phone_label.place(x=100,y=REGISTER_Y+420)
    phone_entry = Entry(frame)
    phone_entry.config(relief="groove")
    phone_entry.place(x=REGISTER_X,y=REGISTER_Y+440,width=REGISTER_PHONE_WIDTH,height=REGISTER_ENTRY_HEIGHT)
    phone_btn = Button(frame)
    phone_btn.config(text="인증번호", relief="flat", bg="orange", foreground="white")
    phone_btn.place(x=REGISTER_PHONE_CHECK_X,y=REGISTER_Y+440,width=REGISTER_PHONE_CHECK_WIDTH,height=REGISTER_ENTRY_HEIGHT)
    phone_check_entry = Entry(frame)
    phone_check_entry.config(relief="groove")
    phone_check_entry.place(x=REGISTER_X,y=REGISTER_Y+470,width=REGISTER_ENTRY_WIDTH,height=REGISTER_ENTRY_HEIGHT)

    register_btn = Button(frame)
    register_btn.config(text="가입하기", relief="flat", bg="orange", foreground='white')
    register_btn.place(x=REGISTER_X,y=REGISTER_Y+520,width=REGISTER_ENTRY_WIDTH,height=REGISTER_ENTRY_HEIGHT+10)

    # frame.mainloop() 없으면 이미지 출력이 안됨.
    frame.mainloop()


login_btn = Button(win)
login_btn.config(text="로그인", relief="flat", bg="orange", foreground='white', command=login_user)
login_btn.place(x=LOGIN_X+30,y=LOGIN_Y+70,width=LOGIN_ENTRY_WIDTH,height=LOGIN_ENTRY_HEIGHT)

password_find_btn = Button(win)
password_find_btn.config(text="비밀번호 찾기", relief="flat")
password_find_btn.place(x=OPTIONS_X,y=OPTIONS_Y)

id_find_btn = Button(win)
id_find_btn.config(text="아이디 찾기", relief="flat")
id_find_btn.place(x=OPTIONS_X+100,y=OPTIONS_Y)

user_register_btn = Button(win)
user_register_btn.config(text="회원 가입", relief="flat", command=register_user)
user_register_btn.place(x=OPTIONS_X+200,y=OPTIONS_Y)

win.mainloop()
