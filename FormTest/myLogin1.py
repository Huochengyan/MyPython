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
            b3['text']='���������û���...'
            return True
        def anw_to_but():
            if str.upper(e1.get())=='ABCD' and e2.get()=='1234':
                b3['text']='��¼�ɹ�'
            else:
                b3['text']='�û�������������!!!'

        b1=tkinter.Label(top,text='�û���:',font=('������κ','16'))
        b1.grid(row=0,column=0)
        b2=tkinter.Label(top,text='����:',font=('������κ','16'))
        b2.grid(row=1,column=0)
        e1=tkinter.Entry(top,font=('����','16'))
        v=tkinter.StringVar()
        e1['textvariable']=v
        e1['validate']='key'
        e1['validatecommand']=isok
        e1.grid(row=0,column=1)
        e1.focus_force()
        e2=tkinter.Entry(top,font=('����','16'))
        e2['show']='*'
        e2.grid(row=1,column=1)
        but=tkinter.Button(top,text='ȷ��',font=('����','16'),command=anw_to_but)
        but.grid(row=2,column=2,padx=10,pady=10)
        b3=tkinter.Label(top,text='��Ϣ��ʾ��',font=('������κ','16'),relief='ridge',width=24)
        b3.grid(row=2,column=0,pady=10,columnspan=2,sticky='SW')
        top.mainloop()
   
        
