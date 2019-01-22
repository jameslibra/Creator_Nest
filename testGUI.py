from tkinter import *
root = Tk()

text1 = Text(root,width=30,height=40)
#INSERT索引表示在光标处插入
text1.insert(INSERT,'I Love')
#END索引号表示在最后插入
text1.insert(END,' you')
text1.pack()
mainloop()