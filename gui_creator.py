#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : gui_creator.py
# Author: Wangyuan
# Date  : 2019-1-3
from OutputDocx import *
from GetExcelInfo import *
from DrawCreator import *
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilenames
from re import sub
def gui_creator():
    #图形界面设计
    w = tk.Tk()
    w.title('排料之光')
    sw = w.winfo_screenwidth()
    # 得到屏幕宽度
    sh = w.winfo_screenheight()
    ww = 800
    wh = 400
    x = (sw - ww) / 2
    y = (sh - wh) / 2
    # 得到屏幕高度
    w.geometry("%dx%d+%d+%d" %(ww,wh,x,y))

    #创建显示框
    # frame_r=tk.Frame(w,height= 400,width = 300,bg='red')
    # frame_r.pack(side='right',padx=10,pady=10)
    frame_l=tk.Frame(w,height= 400,width = 300)
    frame_l.pack(side='left',padx=10,pady=10)
    # result1 = tk.StringVar()
    # result2 = tk.StringVar()
    # result3 = tk.StringVar()
    # result4 = tk.StringVar()
    # global result5,result6
    # result5 = tk.StringVar()
    # result6 = tk.StringVar()
    # 显示输出结果
    # tk.Label(frame_r, textvariable=result1).pack()
    # tk.Label(frame_r, textvariable=result2).pack()
    # tk.Label(frame_r, textvariable=result3).pack()
    # tk.Label(frame_r, textvariable=result4).pack()
    # tk.Label(frame_r, textvariable=result5).pack()
    # tk.Label(frame_r, textvariable=result6).pack()

    def sel_doc():
        path_ = askopenfilenames(filetypes=[("text file", "*.xlsx"), ("all", "*.*")], )
        path.set(path_)
        path.get()
        addrs = path.get().strip('(').strip(')').split(',')
        for addr in addrs:
            lb.insert(END,addr.strip('\'').split('/')[-1])

    def let_work():
        if  path.get():
            addr = path.get().strip('(').strip(')').split(',')
            for ad in addr:
                if ad!= '':
                    g = GetExcelInfo(ad.strip().strip('\''))
                    info=g.output
                    error=g.error

                    doc_addr = '/'.join(ad.strip().strip('\'').split('/')[:-1])
                    for i in g.output:
                        try:
                            DrawCreator(i['name'], i['type'], i['parameter'], i['material'], i['thickness'], address=doc_addr)
                        except BaseException:
                            print(i['name'], i['type'], i['parameter'], i['material'], i['thickness'])
                            print('绘图错误请检查！！！')
                    addinfo(info)
                    adderror(error)
        else:
            messagebox.showinfo(title='提示', message='至少选择一个Excel文件')

    def addinfo(info):
        for i in info:
            infoBox.insert(END,i['name']+str(i['parameter'])+'\n'+'\n')

    def adderror(error):
        for i in error:
            errorBox.insert(END, i+'\n'+'\n')
    def clear():
        infoBox.delete('1.0',END)
        errorBox.delete('1.0',END)
        lb.delete(0,END)
        path.set('')
    def let_docx_work():
        if path.get():
            addr = path.get().strip('(').strip(')').split(',')
            for ad in addr:
                if ad != '':
                    xls_addr = ad.strip().strip('\'')
                    g = GetExcelInfo(xls_addr)
                    print(g.docx_list)
                    OutputDocx(g.docx_list,address=xls_addr)

        else:
             messagebox.showinfo(title='提示', message='至少选择一个Excel文件')
        # result5.set('文件已生成')

    # sb = Scrollbar(frame_l)
    # sb.pack(side=RIGHT, fill=Y)
    tk.Label(frame_l, text="目标路径:").pack(side=TOP)
    path = tk.StringVar()
    # tk.Entry(frame_l, textvariable = path).pack()
    lb=tk.Listbox(frame_l)
                  # , yscrollcommand=sb.set)
    lb.pack()
    # sb.config(command=lb.yview)
    tk.Button(frame_l,text='选择文件所在位置',command=sel_doc).pack(pady='10')
    # tk.Button(frame_l,text='选择文件夹所在位置',command=sel_doc).grid(row=0
    tk.Button(frame_l,text='一键生成dxf数据',command=let_work).pack(pady='10')
    tk.Button(frame_l,text='一键生成下料清单',command=let_docx_work).pack(pady='10')
    tk.Label(w, text="提示信息").pack()
    infoBox=tk.Text(w,width=100,height=10)
    infoBox.pack(padx=10,pady=10)
    tk.Label(w, text="错误报障").pack()
    errorBox=tk.Text(w, width=100, height=10)
    errorBox.pack(padx=10,pady=10)
    tk.Button(w, text='Clear',command=clear ).pack()
    w.mainloop()

gui_creator()