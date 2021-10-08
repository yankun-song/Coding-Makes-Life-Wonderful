#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import messagebox
import pygame as py

root = Tk()
# program title
root.title("Happy Birthday to 11")
# program icon 
root.iconbitmap("matplotlib\panda2.ico")

flag1, flag2, flag3, flag4, flag5 = 0, 0, 0, 0, 0


py.mixer.init()
py.mixer.music.load("matplotlib/birthdaysong.mp3")
py.mixer.music.play(-1, 10)

#####################################
############检查答案函数################
#####################################
def popup():
    flag = flag1 and flag2 and flag3 and flag4 and flag5
    if flag:
        messagebox.showinfo("熊猫有话说", "开箱密码：xiongmaoxihuanguaishouyou")
    else:
        messagebox.showwarning("熊猫有话说", "问题还没全答对呢！")


def checkAns1():
    if a1.get() in ["陈瑶", "小瑶子", "怪兽游"]:
        messagebox.showinfo("熊猫有话说", "哎呦不错哦！")
        global flag1 
        flag1 = 1
    else:
        messagebox.showwarning("熊猫有话说", "怎么回事？？？再想想！！！")

def checkAns2():
    if a2.get() in ["天蝎座", "天蝎"]:
        messagebox.showinfo("熊猫有话说", "哎呦不错哦！")
        global flag2 
        flag2 = 1
    else:
        messagebox.showwarning("熊猫有话说", "怎么回事？？？再想想！！")

def checkAns3():
    if a3.get() in  ["熊猫", "可可", "小可子"] :
        messagebox.showinfo("熊猫有话说", "哎呦不错哦！")
        global flag3 
        flag3 = 1
    else:
        messagebox.showwarning("熊猫有话说", "怎么回事？？？再想想！！")

def checkAns4():
    if a4.get() in ["10", "10年","十年"]:
        messagebox.showinfo("熊猫有话说", "哎呦不错哦！")
        global flag4 
        flag4 = 1
    else:
        messagebox.showwarning("熊猫有话说", "怎么回事？？？再想想！！")
        
def checkAns5():
    if a5.get() in ["天生姐妹命", "天生姐妹命！"]:
        messagebox.showinfo("熊猫有话说", "哎呦不错哦！")
        global flag5 
        flag5 = 1
    else:
        messagebox.showwarning("熊猫有话说", "怎么回事？？？再想想！！")

    
    
    
#####################################
############提问区####################
#####################################

# Q1
# 设置问题
q1= Label(root, text="你是谁哇？")
q1.grid(row=0,column=0, sticky='w')
# 要求答案
a1 = Entry(root, width=35, borderwidth=5)
a1.grid(row=0, column=1,  padx=10, pady=10)
# 检查答案
c1 = Button(root, text="check", command=checkAns1)
c1.grid(row=0, column=2)

# Q2
q2= Label(root, text="你是哪个星座的呀？")
q2.grid(row=1,column=0, sticky='w')
a2 = Entry(root, width=35, borderwidth=5)
a2.grid(row=1, column=1,  padx=10, pady=10)
c2 = Button(root, text="check", command=checkAns2)
c2.grid(row=1, column=2)

# Q3
q3= Label(root, text="你最好的朋友是谁呢？")
q3.grid(row=2,column=0, sticky='w')
a3 = Entry(root, width=35, borderwidth=5)
a3.grid(row=2, column=1,  padx=10, pady=10)
c3 = Button(root, text="check", command=checkAns3)
c3.grid(row=2, column=2)

# Q4
q4= Label(root, text="你和她认识多少年啦？")
q4.grid(row=3,column=0, sticky='w')
a4 = Entry(root, width=35, borderwidth=5)
a4.grid(row=3, column=1,  padx=10, pady=10)
c4 = Button(root, text="check", command=checkAns4)
c4.grid(row=3, column=2)

# Q5
q5= Label(root, text="你们的友谊宣言是？")
q5.grid(row=4,column=0, sticky='w')
a5 = Entry(root, width=35, borderwidth=5)
a5.grid(row=4, column=1,  padx=10, pady=10)
c5 = Button(root, text="check", command=checkAns5)
c5.grid(row=4, column=2)

Button(root, text="快来领取礼物钥匙吧！", command=popup).grid(row=5,columnspan=3)





root.mainloop()


# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




