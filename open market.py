from tkinter import *
from tkinter.font import Font
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import pandas as pd

# print(Tcl().eval('info patchlevel'))
# print(pd.__version__)
# print(PIL.__version__)

# 왜 GUI에 클래스가 필요한걸까?

# Image Size
LOGO_WIDTH = 100
LOGO_HEIGHT = 100
LOGIN_WIDTH = 20
LOGIN_HEIGHT = 20
BACK_WIDTH = 30
BACK_HEIGHT = 30

# Widget coordinate
LOGO_X = 150
LOGO_Y = 30
LOGIN_X = 100
LOGIN_Y = 210
LOGIN_ERROR_X = LOGIN_X+30
LOGIN_ERROR_Y = LOGIN_Y+110
OPTIONS_X = 70
OPTIONS_Y = 350
REGISTER_X = 100
REGISTER_Y = 20

# Widget area
LOGIN_ENTRY_WIDTH = 150
LOGIN_ENTRY_HEIGHT = 30
REGISTER_ENTRY_WIDTH = 200
REGISTER_ENTRY_HEIGHT = 25
REGISTER_BIRTH_WIDTH = 64
REGISTER_GENDER_HEIGHT = 30
REGISTER_PHONE_WIDTH = 140
REGISTER_PHONE_CHECK_X = 244
REGISTER_PHONE_CHECK_WIDTH = 56

def load_df_user():
    df_user = pd.read_csv('csv/user.csv')
    df_user.set_index(df_user['USER_ID'], inplace=True)
    return df_user

def login():
    df_user = load_df_user()
    id = id_entry.get()
    pw = password_entry.get()
    if id == "":
        login_error_label.config(text="아이디를 입력해 주세요.", foreground="red")
        login_error_label.place(x=LOGIN_ERROR_X,y=LOGIN_ERROR_Y)
        return 0
    else:
        if pw == "":
            login_error_label.config(text="비밀번호를 입력해 주세요.", foreground="red")
            login_error_label.place(x=LOGIN_ERROR_X,y=LOGIN_ERROR_Y)
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
        login_error_label.config(text="아이디(로그인 전용 아이디) 또는 비밀번호를 잘못 입력했습니다.\n입력하신 내용을 다시 확인해주세요.", foreground="red")
        login_error_label.place(x=LOGIN_ERROR_X-115,y=LOGIN_ERROR_Y)

def register_user():
    root.title("회원가입")
    root.geometry("400x600")
    login_frame.place_forget()
    register_frame.place(width=400,height=600)

def back():
    root.title("로그인")
    root.geometry("400x400")
    id_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    register_frame.place_forget()
    login_frame.place(width=400,height=400)

def register():
    id = id_entry2.get()
    pw = password_entry2.get()
    

root = Tk()
default_font = Font(family="TkDefaultFont",size=10)
root.option_add("*Font", default_font)
root.resizable(width=FALSE, height=FALSE)
root.iconbitmap('img/Open Market.ico')
root.title("로그인")
root.geometry("400x400")

login_frame = Frame(root)

logo_img = ImageTk.PhotoImage(Image.open('img/logo.png').resize((LOGO_WIDTH, LOGO_HEIGHT)))
id_img = ImageTk.PhotoImage(Image.open('img/id.png').resize((LOGIN_WIDTH, LOGIN_HEIGHT)))
password_img = ImageTk.PhotoImage(Image.open('img/password.png').resize((LOGIN_WIDTH, LOGIN_HEIGHT)))

logo_label = Label(login_frame)
title_label = Label(login_frame)
id_label = Label(login_frame)
password_label = Label(login_frame)
login_error_label = Label(login_frame)

logo_label.config(image=logo_img)
title_label.config(text="Open Market",font=('Impact', 20),foreground='orange')
id_label.config(image=id_img)
password_label.config(image=password_img)

logo_label.place(x=LOGO_X,y=LOGO_Y)
title_label.place(x=LOGO_X-20,y=LOGO_Y+120)
id_label.place(x=LOGIN_X,y=LOGIN_Y)
password_label.place(x=LOGIN_X,y=LOGIN_Y+30)

id_var = StringVar(login_frame)
password_var = StringVar(login_frame)

id_entry = Entry(login_frame)
password_entry = Entry(login_frame)

id_entry.config(textvariable=id_var, relief="groove")
password_entry.config(textvariable=password_var, show="*", relief="groove")

id_entry.place(x=LOGIN_X+30,y=LOGIN_Y, width=LOGIN_ENTRY_WIDTH,height=LOGIN_ENTRY_HEIGHT)
password_entry.place(x=LOGIN_X+30,y=LOGIN_Y+30, width=LOGIN_ENTRY_WIDTH,height=LOGIN_ENTRY_HEIGHT)

login_frame.place(width=400,height=400)

login_btn = Button(login_frame)
find_password_btn = Button(login_frame)
find_id_btn = Button(login_frame)
register_user_btn = Button(login_frame)

login_btn.config(text="로그인", relief="flat", bg="orange", foreground='white', command=login)
login_btn.place(x=LOGIN_X+30,y=LOGIN_Y+70,width=LOGIN_ENTRY_WIDTH,height=LOGIN_ENTRY_HEIGHT)

find_password_btn.config(text="비밀번호 찾기", relief="flat")
find_id_btn.config(text="아이디 찾기", relief="flat")
register_user_btn.config(text="회원 가입", relief="flat", command=register_user)

find_password_btn.place(x=OPTIONS_X,y=OPTIONS_Y)
find_id_btn.place(x=OPTIONS_X+100,y=OPTIONS_Y)
register_user_btn.place(x=OPTIONS_X+200,y=OPTIONS_Y)


# register
register_frame = Frame(root)

back_img = ImageTk.PhotoImage(Image.open('img/back.png').resize((BACK_WIDTH,BACK_HEIGHT)))

id_var2 = StringVar(register_frame)
password_var2 = StringVar(register_frame)
password_reconfirm_var = StringVar(register_frame)
name_var = StringVar(register_frame)
birth_year_var = StringVar(register_frame)
birth_day_var = StringVar(register_frame)
phone_var = StringVar(register_frame)
phone_check_var = StringVar(register_frame)

def id_var2_length(*args):
    s = id_var2.get()
    if len(s) > 20:
        id_var2.set(s[:20])

def password_var2_length(*args):
    s = password_var2.get()
    if len(s) > 20:
        password_var2.set(s[:20])

def password_reconfirm_var_length(*args):
    s = password_reconfirm_var.get()
    if len(s) > 20:
        password_reconfirm_var.set(s[:20])

def name_var_length(*args):
    s = name_var.get()
    if len(s) > 40:
        name_var.set(s[:40])

def birth_year_var_length(*args):
    s = birth_year_var.get()
    if len(s) > 4:
        birth_year_var.set(s[:4])
    
def birth_day_var_length(*args):
    s = birth_day_var.get()
    if len(s) > 2:
        birth_day_var.set(s[:2])    

def phone_var_length(*args):
    s = phone_var.get()
    if len(s) > 13:
        phone_var.set(s[:13])

def phone_check_var_length(*args):
    s = phone_check_var.get()
    if len(s) > 16:
        phone_check_var.set(s[:4])

id_var2.trace_variable("w", id_var2_length)
password_var2.trace_variable("w", password_var2_length)
password_reconfirm_var.trace_variable("w", password_reconfirm_var_length)
name_var.trace_variable("w", name_var_length)
birth_year_var.trace_variable("w", birth_year_var_length)
birth_day_var.trace_variable("w", birth_day_var_length)
phone_var.trace_variable("w", phone_var_length)
phone_check_var.trace_variable("w", phone_check_var_length)

back_btn = Button(register_frame)
back_btn.config(image=back_img, relief="flat", command=back)
back_btn.place(x=0,y=0)

id_label2 = Label(register_frame)
password_label2 = Label(register_frame)
password_reconfirm_label = Label(register_frame)
name_label = Label(register_frame)
birth_label = Label(register_frame)
gender_label = Label(register_frame)
phone_label = Label(register_frame)

id_label2.config(text="아이디")
password_label2.config(text="비밀번호")
password_reconfirm_label.config(text="비밀번호 재확인")
name_label.config(text="이름")
birth_label.config(text="생년월일")
gender_label.config(text="성별")
phone_label.config(text="휴대전화")

id_entry2 = Entry(register_frame)
password_entry2 = Entry(register_frame)
password_reconfirm_entry = Entry(register_frame)
name_entry = Entry(register_frame)
birth_year_entry = Entry(register_frame)
birth_month_combo = Combobox(register_frame)
birth_day_entry = Entry(register_frame)
gender_combo = Combobox(register_frame)
phone_entry = Entry(register_frame)
phone_check_entry = Entry(register_frame)

id_entry2.config(relief="groove", textvariable=id_var2)
password_entry2.config(show='*',relief="groove", textvariable=password_var2)
password_reconfirm_entry.config(show='*',relief="groove", textvariable=password_reconfirm_var)
name_entry.config(relief="groove", textvariable=name_var)
birth_year_entry.config(relief="groove", textvariable=birth_year_var)
birth_month_combo.config(values=["월", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], state="readonly")
birth_month_combo.current(0)
birth_day_entry.config(relief="groove", textvariable=birth_day_var)
gender_combo.config(values=["성별", "남자", "여자", "선택 안함"], state="readonly")
gender_combo.current(0)
phone_entry.config(relief="groove", textvariable=phone_var)
phone_check_entry.config(relief="groove", textvariable=phone_check_var, state="disabled")

id_label2.place(x=REGISTER_X,y=REGISTER_Y)
password_label2.place(x=REGISTER_X,y=REGISTER_Y+70)
password_reconfirm_label.place(x=REGISTER_X,y=REGISTER_Y+140)
name_label.place(x=REGISTER_X,y=REGISTER_Y+210)
birth_label.place(x=REGISTER_X,y=REGISTER_Y+280)
gender_label.place(x=100,y=REGISTER_Y+350)
phone_label.place(x=100,y=REGISTER_Y+420)

id_entry2.place(x=REGISTER_X,y=REGISTER_Y+20, width=REGISTER_ENTRY_WIDTH,height=REGISTER_ENTRY_HEIGHT)
password_entry2.place(x=REGISTER_X,y=REGISTER_Y+90, width=REGISTER_ENTRY_WIDTH,height=REGISTER_ENTRY_HEIGHT)
password_reconfirm_entry.place(x=REGISTER_X,y=REGISTER_Y+160, width=REGISTER_ENTRY_WIDTH,height=REGISTER_ENTRY_HEIGHT)
name_entry.place(x=REGISTER_X,y=REGISTER_Y+230, width=REGISTER_ENTRY_WIDTH,height=REGISTER_ENTRY_HEIGHT)
birth_year_entry.place(x=REGISTER_X,y=REGISTER_Y+300, width=REGISTER_BIRTH_WIDTH,height=REGISTER_ENTRY_HEIGHT)
birth_month_combo.place(x=REGISTER_X+68,y=REGISTER_Y+300, width=REGISTER_BIRTH_WIDTH,height=REGISTER_ENTRY_HEIGHT)
birth_day_entry.place(x=REGISTER_X+136,y=REGISTER_Y+300, width=REGISTER_BIRTH_WIDTH,height=REGISTER_ENTRY_HEIGHT)
gender_combo.place(x=REGISTER_X,y=REGISTER_Y+370, width=REGISTER_ENTRY_WIDTH,height=REGISTER_GENDER_HEIGHT)
phone_entry.place(x=REGISTER_X,y=REGISTER_Y+440, width=REGISTER_PHONE_WIDTH,height=REGISTER_ENTRY_HEIGHT)
phone_check_entry.place(x=REGISTER_X,y=REGISTER_Y+470, width=REGISTER_ENTRY_WIDTH,height=REGISTER_ENTRY_HEIGHT)

phone_btn = Button(register_frame)
phone_btn.config(text="인증번호", relief="flat", bg="orange", foreground="white")
phone_btn.place(x=REGISTER_PHONE_CHECK_X,y=REGISTER_Y+440,width=REGISTER_PHONE_CHECK_WIDTH,height=REGISTER_ENTRY_HEIGHT)

register_btn = Button(register_frame)
register_btn.config(text="가입하기", relief="flat", bg="orange", foreground='white')
register_btn.place(x=REGISTER_X,y=REGISTER_Y+520, width=REGISTER_ENTRY_WIDTH,height=REGISTER_ENTRY_HEIGHT+10)

root.mainloop()