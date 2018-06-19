#-*- coding:GB2312 -*-
# exam Label,Button,Entry
import tkinter

class LoginClass:
    def bar(self):
        print("login  ....")
    def init(self):
        top=tkinter.Tk()
        top.geometry('400x100+0+0')
        top.wm_title('Entry Exam')
        def isok():
            b3['text']='正在输入用户名...'
            return True
        def anw_to_but():
            if str.upper(e1.get())=='ABCD' and e2.get()=='1234':
                b3['text']='登录成功'
            else:
                b3['text']='用户名或密码有误!!!'

        b1=tkinter.Label(top,text='用户名:',font=('华文新魏','16'))
        b1.grid(row=0,column=0)
        b2=tkinter.Label(top,text='密码:',font=('华文新魏','16'))
        b2.grid(row=1,column=0)
        e1=tkinter.Entry(top,font=('宋体','16'))
        v=tkinter.StringVar()
        e1['textvariable']=v
        e1['validate']='key'
        e1['validatecommand']=isok
        e1.grid(row=0,column=1)
        e1.focus_force()
        e2=tkinter.Entry(top,font=('宋体','16'))
        e2['show']='*'
        e2.grid(row=1,column=1)
        but=tkinter.Button(top,text='确定',font=('宋体','16'),command=anw_to_but)
        but.grid(row=2,column=2,padx=10,pady=10)
        b3=tkinter.Label(top,text='信息提示区',font=('华文新魏','16'),relief='ridge',width=24)
        b3.grid(row=2,column=0,pady=10,columnspan=2,sticky='SW')
        top.mainloop()
   
        
