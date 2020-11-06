#!/usr/bin/env python
# coding: utf-8

# In[4]:


from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import pygame as py

root = Tk()
# program title
root.title("熊猫国际无限公司")
# program icon 
root.iconbitmap("matplotlib\panda2.ico")

py.mixer.init()
py.mixer.music.load("matplotlib/music2.mp3")
py.mixer.music.play(-1, 10)



##########################
#######读取图片#############
##########################

my_img1 = ImageTk.PhotoImage(Image.open("matplotlib\zz1.jpg").resize((500, 1000), Image.ANTIALIAS))
my_img2 = ImageTk.PhotoImage(Image.open("matplotlib\zz2.jpg").resize((500, 1000), Image.ANTIALIAS))
my_img3 = ImageTk.PhotoImage(Image.open("matplotlib\zz3.jpg").resize((500, 1000), Image.ANTIALIAS))
my_img4 = ImageTk.PhotoImage(Image.open("matplotlib\zz4.jpg").resize((500, 1000), Image.ANTIALIAS))
my_img5 = ImageTk.PhotoImage(Image.open("matplotlib\zz5.jpg").resize((500, 1000), Image.ANTIALIAS))
my_img6 = ImageTk.PhotoImage(Image.open("matplotlib\zz6.jpg").resize((500, 1000), Image.ANTIALIAS))
my_img7 = ImageTk.PhotoImage(Image.open("matplotlib\zz7.jpg").resize((500, 1000), Image.ANTIALIAS))
my_img8 = ImageTk.PhotoImage(Image.open("matplotlib\zz8.jpg").resize((500, 1000), Image.ANTIALIAS))
my_img9 = ImageTk.PhotoImage(Image.open("matplotlib\zz9.jpg").resize((500, 1000), Image.ANTIALIAS))
my_img10 = ImageTk.PhotoImage(Image.open("matplotlib\zz10.jpg").resize((500, 1000), Image.ANTIALIAS))
my_img11 = ImageTk.PhotoImage(Image.open("matplotlib\zz11.jpg").resize((500, 1000), Image.ANTIALIAS))
my_img12 = ImageTk.PhotoImage(Image.open("matplotlib\zz12.jpg").resize((500, 1000), Image.ANTIALIAS))
my_img = [my_img1,my_img2,my_img3,my_img4,
          my_img5,my_img6,my_img7,my_img8,
         my_img9,my_img10,my_img11,my_img12]

##########################
#######打开窗口#############
##########################
def open2(n):
    #global my_img
    top = Toplevel()
    top.title("请仔细阅读哦")
    top.iconbitmap("matplotlib\panda2.ico")
    
    my_label = Label(top, image=my_img[n-1]).grid(row=0, column=0)
    
    btn2 = Button(top, text="再抽取下一条吧", command=top.destroy).grid(row=1, column=0)


def open1():
    top = Toplevel()
    top.title("熊猫牌锦囊盲盒")
    top.iconbitmap("matplotlib\panda2.ico")    #random.randint(1,11)
    button_1 = Button(top, text="请抽取盲盒！快试试自己的手气吧！", padx=200, pady=200, command=lambda: open2(random.randint(1,11)), bg="#D5F5E3")
    button_2 = Button(top, text="exit", command=lambda: open2(12))
#     button_2 = Button(top, text="2", padx=40, pady=20, command=lambda:| open2(2))
#     button_3 = Button(top, text="3", padx=40, pady=20, command=lambda: open2(3))
#     button_4 = Button(top, text="4", padx=40, pady=20, command=lambda: open2(4))
#     button_5 = Button(top, text="5", padx=40, pady=20, command=lambda: open2(5))
#     button_6 = Button(top, text="6", padx=40, pady=20, command=lambda: open2(6))
#     button_7 = Button(top, text="7", padx=40, pady=20, command=lambda: open2(7))
#     button_8 = Button(top, text="8", padx=40, pady=20, command=lambda: open2(8))
#     button_9 = Button(top, text="9", padx=40, pady=20, command=lambda: open2(9))
#     button_10 = Button(top, text="10", padx=36, pady=20, command=lambda: open2(10))
#     button_11 = Button(top, text="11", padx=36, pady=20, command=lambda: open2(11))
#     button_12 = Button(top, text="", padx=44, pady=20, )
    
    button_1.grid(row=0, column=0)
    button_2.grid(row=1, column=0)
#     button_2.grid(row=0, column=1)
#     button_3.grid(row=0, column=2)
#     button_4.grid(row=1, column=0)
#     button_5.grid(row=1, column=1)
#     button_6.grid(row=1, column=2)
#     button_7.grid(row=2, column=0)
#     button_8.grid(row=2, column=1)
#     button_9.grid(row=2, column=2)
#     button_10.grid(row=3, column=0)
#     button_11.grid(row=3, column=1)
#     button_12.grid(row=3, column=2)







##########################
#######检查答案#############
##########################

def checkAns1():
    if a1.get() == "xiongmaoxihuanguaishouyou":
    #if True:
        messagebox.showinfo("熊猫有话说", "准备好迎接惊喜了吗？")    
        btn = Button(root, text="请抽取你的11个生日盲盒吧！", command=open1).grid(row=1, columnspan=3)
    else:
        messagebox.showwarning("熊猫有话说", "密码不对啊！再重新闯关吧 ！")


# 检查密码
# 设置问题
q1= Label(root, text="请输入熊猫牌盲盒密码：")
q1.grid(row=0,column=0, sticky='w')
# 要求答案
a1 = Entry(root, width=35, borderwidth=5)
a1.grid(row=0, column=1,  padx=10, pady=10)
# 检查答案
c1 = Button(root, text="确认", command=checkAns1)
c1.grid(row=0, column=2)

root.mainloop()


# In[35]:


import pygame as py


# In[ ]:





# In[ ]:




