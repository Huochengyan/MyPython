'''
需求描述：编写一个图形用户界面程序
（1）创建一个主窗体（顶层窗体），为其设置tile改性，内容任意
（2）要求有菜单项（主菜单File,Edit，子菜单）
其中，点击“File菜单下的Exit子菜单可以关闭窗体,其他菜单项不实现具体功能。

（3）往窗体上添加一个“标签（label)”控件和一个“按钮(butten)”，
点击butten，能实现关闭窗体功能。

'''
import tkinter

from FormTest.myLogin1 import LoginClass

top=tkinter.Tk()
'''这时在桌面上创建了一个顶层窗体对象top,GUI的其他组件都要在top中创建
tkinter是模块，Tk()是类，top是对象（是Tk()类的一个实例）

'''
top.wm_title('这是窗体的标题，Python（GUI）用户界面')
top.geometry('600x400+0+0')

'''
顶层窗体创建好之后，可以往里面添加其他控件，例如，标签，
按钮，输入框，菜单，滚动条等
'''
lb_1=tkinter.Label(top,text='这是窗体上的一个标签，Hello World')
lb_1.pack(side='top')    #使用lb_1对象的pack()方法，把控件布局到窗体上

button = tkinter.Button(top,text=" 退出 ",foreground='red',cursor='man',command=top.destroy)
button.pack(side='left')
##################### login #####################################
def btnLogin():
    print("this login info ")
    obj=LoginClass()
    obj.init();


button = tkinter.Button(top,text=" Login ",foreground='red',cursor='man',command=btnLogin)
button.pack(side='top')
##################### login #####################################
main_m=tkinter.Menu(top)
top['menu']=main_m                                  #指定顶层菜单

'''File菜单项的定义 '''
item_File=tkinter.Menu(main_m,tearoff=0)
for i in['New','Open']:
    item_File.add_command(label=i)
item_File.add_separator()                           #添加一个菜单项分割线
for i in['Save','Save as']:
    item_File.add_command(label=i)
item_File.add_separator()
item_File.add_command(label='Exit',command=top.destroy)                 #单独添加一个菜单项

main_m.add_cascade(label='File',menu=item_File)     #定义级连

'''Edit菜单项的定义 '''
item_Edit=tkinter.Menu(main_m,tearoff=0)
for i in['Copy','Cut','Paste']:
    item_Edit.add_command(label=i)                  #指定菜单项
main_m.add_cascade(label='Edit',menu=item_Edit)     #定义级连

top.mainloop()      #进入主事件循环


