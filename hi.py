from turtle import *
from tkinter import *
from tkinter import ttk

fen1 = Tk()  #  لصنع دالة من خلالها تتحكم في الواجه أو الصفحة
# # fen1.title("Test #")  # تغير اسم الصفحة
# fen1.geometry('400x400+590+240')  # تحديد عرض وطول الصفحة وحتى موقع ظهور الصفحة 
# # fen1.resizable(False, True)  #   خاصية للسماح للمستخأن يكبر او لا يكبر الصفحة أما من الطول أو العرض
# # fen1.minsize(300, 300) #  أقل حجم لتصغير الصفحة من الطول والعرض
# # fen1.maxsize(800, 600)  #  أكثر حجم لتكبير الصفحة من الطول أو العرض
# # fen1.option_add('*font', 'Times 10')  #  تغير نوع الخط
# # fen1.attributes('-alpha', 1)  #   شفافية الصفحة
# # text1 = Label(fen1, text='Bonjour tout le monde !', fg='red', bg='green')  #   للكتابة داخل الصفحة ويمكن تغير لون الخط وخلفية الخط
# # text1.pack()  #  لتشغيل الامر الكتابة على الصفحة
# # bou1 = Button(fen1, text='Quitter', command= fen1.destroy, fg='blue', bg='red')  #   صناعة زر 
# # bou1.pack()  
# # bou2 = Canvas(fen1, bg='dark grey', height=200, width=200)    # لأنشاء صفحة داخل الصفحة
# mod1 = ttk.Label(fen1, text='Hello world', background='red', foreground='blue') 
# mod1.grid(row=2, column=3)
# mod2 = ttk.Button(fen1, text='Hello', command= fen1.destroy,)
# # mod2.pack(ipad=100, side=BOTTOM)    #  side = LEFT, RIGHT, TOP, BOTTOM  && pad(padx=20 , pady=20), | ipad(ipady=20, ipadx=20)
# # mod2.place(x=180, y=170)   


# # mod1.config(text='hello world', foreground='red')
# # mod1['text']='Hi!'
# # mod1['foreground']='green'


# main_window = Tk()
# main_window.geometry('500x500+600+250')
# L0 = Label(main_window, text='أسود', bg='black', fg='white')
# L0.grid(row=0, column=0)
# L1 = Label(main_window, text="أحمر",bg="red", fg="white")
# L1.grid(row=1, column=3)
# L2 = Label(main_window, text="أخضر", bg="green", fg="white")
# L2.grid(row=2, column=6)
# L3 = Label(main_window, text="أزرق", bg="blue", fg="white")
# L3.grid(row=3, column=9)
# main_window.columnconfigure(index=2, weight=20)
# main_window.rowconfigure(index=2, weight=10)
# main_window.mainloop()

# coll = LabelFrame(fen1, width=300, height=300, background='red', text='LEFT')
# coll.pack(side=LEFT)
# colld = LabelFrame(fen1, width=300, height=300, background='blue', text='RIGHT')
# colld.pack(side=RIGHT)
# colled = LabelFrame(fen1, width=300, height=300, background='green', text='TOP')
# colled.pack(side=TOP)
# coller = LabelFrame(fen1, width=300, height=300, background='yellow', text='BOTTOM')
# coller.pack(side=BOTTOM)


# main_window = Tk()
# main_window.title(" الإطارات ") 

# top_frame=Frame(main_window,bg='red')
# top_frame.pack(side='top')
# top_button=Button(top_frame,text=' زرار في إطار علوي' )
# top_button.pack(padx = 40, pady = 40)

# right_frame=Frame(main_window,bg='green')
# right_frame.pack(side='right')
# right_button=Button(right_frame,text=' زرار في إطار على اليمين' )
# right_button.pack(padx = 40, pady = 40)

# left_frame=Frame(main_window,bg='blue')
# left_frame.pack(side='left')
# right_button=Button(left_frame,text=' زرار في إطار على اليسار' )
# right_button.pack(padx = 40, pady = 40)

# bottom_frame=Frame(main_window,bg='yellow')
# bottom_frame.pack(side='bottom')
# bottom_button=Button(bottom_frame,text=' زرار في إطار سفلي' )
# bottom_button.pack(padx = 40, pady = 40)
# main_window.mainloop()

# fen1.option_add("*font", "Stencil 20 bold italic")  # Stencil, نوع الخط , وحجم
# coll = Frame(fen1, background='red', bd=3, relief='solid')
# coll.pack(side='top')
# col = Label(coll, text='Hello World', cursor='star')  # 
# col.pack(padx=40, pady=40)


# main_window = Tk()
# main_window.title(" حاوية العنوان ")

# First_Label = Label(main_window, text="Sample text ",\
# font=("Stencil", "30", "bold italic") ,\
#            fg ="#FFFFFF" , bg="blue", cursor ="star",)

# First_Label.pack(padx=50, pady=50 ,ipadx=100,ipady=100 ,side= TOP)

# main_window.mainloop()


# Mytext = StringVar()
# Name = Label(fen1, textvariable=Mytext)
# Name.pack()


# MyPhoto = PhotoImage(file='OIP.png')
# image = Label(fen1, image=MyPhoto, text="Anime 💕", compound='top')
# image.pack(padx=20, pady=20, ipadx=200, ipady=200, side=TOP)

fen1.geometry('400x400+600+200')
enter = Entry(fen1, bd=3, state="normal")
enter.insert(2, "Name: ")
enter.pack()


fen1.mainloop()
