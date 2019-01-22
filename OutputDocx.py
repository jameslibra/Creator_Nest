#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : OutputDocx.py
# Author: Wangyuan
# Date  : 2019-1-3
from GetExcelInfo import *
from docx import Document
from docx.shared import Mm
from docx.shared import Pt
from docx.oxml.ns import qn
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
import time
from os import getcwd,path,chdir
from glob import glob

#改写成一个类
def OutputDocx(info,address):
    addr = '/'.join(address.strip().strip('\'').split('/')[:-1])
    chdir(addr)
    # doc = Document(docx=path.join(getcwd(), 'default.docx'))
    doc = Document()
    if address.find('排料清单') != -1:
        table_title = str(address.split('\\')[-1].split('/')[-1].split('_')[0].split('-')[0].split(' ')[0])
    else:
        table_title = str(address.split('\\')[-1].split('/')[-1].split(' ')[0])


    #设置全局字体
    doc.styles['Normal'].font.name = u'宋体'
    doc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
    #设置word文件的页面属性
    sections = doc.sections
    sections[0].page_width = Mm(297)
    sections[0].page_height = Mm(210)
    #添加基本内容
    tit = doc.add_paragraph('结构件下料指导书')
    #新设置一种名为"title_style"的新style,设置字体大小，字体样式
    title_style = doc.styles.add_style('UserStyle1', WD_STYLE_TYPE.PARAGRAPH)
    title_style.font.size = Pt(22)
    title_style.font.bold =True
    title_style.font.name = u'宋体'
    title_style._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
    tit.paragraph_format.alignment = WD_TABLE_ALIGNMENT.CENTER
    #为标题应用样式
    tit.style = title_style

    #添加内容，绘制表头
    title_list = [r'序号',r'产品代号', r'零件名称', r'材料',u'厚度',u'下料净尺寸(mm)',u'数量',r'备注']
    trow = len(info) + 2
    tcol = len(title_list)
    table = doc.add_table(rows=trow, cols=tcol, style='Table Grid')
    table.cell(0,0).merge(table.cell(0,tcol-1))  #合并第一行

    # 新设置一种名为"Bold_style"的新style,设置字体大小，字体样式
    Bold_style = doc.styles.add_style('UserStyle2', WD_STYLE_TYPE.CHARACTER)
    Bold_style.font.size = Pt(14)
    Bold_style.font.bold = True
    Bold_style.font.name = u'宋体'
    Bold_style._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
    # 为表注应用样式
    run = table.cell(0,0).paragraphs[0].add_run("  合同号：%s"%table_title+"                     文件编号：JXL-%s-001"%table_title)
    table.cell(0, 0).vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    run.style = Bold_style

    #设置表格内的字体
    table.style.font.size = Pt(12)
    table.style.font.name = u'微软雅黑'
    table.style._element.rPr.rFonts.set(qn('w:eastAsia'), u'微软雅黑')

    #设置表格对其方式
    table.alignment = WD_TABLE_ALIGNMENT.CENTER  #WD_TABLE_ALIGNMENT.LEFT|WD_TABLE_ALIGNMENT.RIGHT 其他设置方式

   # 新设置一种名为"tbhead"的新style,设置字体大小，字体样式
    tbhead = doc.styles.add_style('UserStyle3', WD_STYLE_TYPE.CHARACTER)
    tbhead.font.size = Pt(12)
    tbhead.font.bold = True
    tbhead.font.name = u'宋体'
    tbhead._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')

    #设置表格的表头的样式为table_head
    for i, value in enumerate(title_list):
        run_1 = table.cell(1, i).paragraphs[0].add_run(value)
        table.cell(1, i).paragraphs[0].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        table.cell(1, i).vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        run_1.style = tbhead
    # 设置表格内容及对其方式
    y = 0
    for list in info:
        x = 1
        #设置每一行第一个单元格的数值
        table.cell(y + 2, 0).text = str(y+1)
        table_result ='数据已处理: '+str(int((y+1)/len(info) *100 ))+ '%'
        print(table_result)

        table.cell(y + 2, 0).paragraphs[0].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        table.cell(y + 2, 0).vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        #设置每一行的单元格的内容
        table.cell(y + 2, 1).text = str(list['product_code'])
        table.cell(y + 2, 2).text = str(list['part_name'])
        table.cell(y + 2, 3).text = str(list['material'])
        table.cell(y + 2, 4).text = str(list['thickness'])
        table.cell(y + 2, 5).text = str(list['size'])
        table.cell(y + 2, 6).text = str(list['sum'])
        for x in range(tcol):
            table.cell(y + 2, x).paragraphs[0].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            table.cell(y + 2, x).vertical_alignment = WD_ALIGN_VERTICAL.CENTER

        y += 1
    print('数据已处理完毕，请耐心等待')
    #设置列宽
    table.autofit = False
    for i in range(trow):
        table.cell(i,0).width = Mm(15)
        table.cell(i,1).width = Mm(45)
        table.cell(i,2).width = Mm(30)
        table.cell(i,3).width = Mm(30)
        table.cell(i,4).width = Mm(20)
        table.cell(i,5).width = Mm(65)
        table.cell(i,6).width = Mm(18)
        table.cell(i,7).width = Mm(22)
        # 设置行高
        table.rows[i].height = Mm(11)


    #设置表格第一行的对齐方式为左对齐
    table.cell(0, 0).paragraphs[0].paragraph_format.alignment =WD_ALIGN_PARAGRAPH.LEFT
    par1 = doc.add_paragraph('')
    par2 = doc.add_paragraph('')
    par1.paragraph_format.space_after =0
    par2.paragraph_format.space_after =0
    par2.paragraph_format.space_before =Pt(6)
    mark1 = par1.add_run(u'\n  备注:')
    mark2 = par1.add_run(
                         u'\n        完成后请做好标识，标识内容包括：合同号、产品代号、零件号、尺寸。')
    mark3 = par2.add_run(u'           编制:王元 %s。'%time.strftime('%Y-%m-%d',time.localtime(time.time()))
                        +'                  审核:刘光 %s。'%time.strftime('%Y-%m-%d',time.localtime(time.time())))
    mark1.style = Bold_style
    mark2.style = Bold_style
    mark3.style = Bold_style
    #设定页边距为上18mm.下15mm
    doc.sections[0].top_margin = Mm(18)
    doc.sections[0].bottom_margin = Mm(15)
    #文件保存
    doc.save(addr +'\\' + table_title + u'_结构件下料清单.docx')
    table_finish = '文件已生成'
    print(table_finish)
