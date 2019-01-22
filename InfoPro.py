#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : InfoPro.py
# Author: Wangyuan
# Date  : 2019-1-4
from re import match,sub
from pandas import read_excel,DataFrame
class InfoPro:

    def __init__(self,addr):
        self.form_out = []
        self.omit_value = []
        self.addr = addr
        df = read_excel(addr)
        line_len = len(df.values)
        print(line_len)
        for line in df.values:
            form_out = {}
            # 对应excel中的通径
            form_out[1] = addr.split('/')[-1].split(' ')[0]
            # 对应excel中的件数
            form_out[2] = 1
            # 对应excel中的零件名称
            form_out[3] = sub('\*','X',line[2])
            # 对应excel中的数量
            form_out[9]= line[7]
            # 对应excel中的材料
            form_out[4] = line[3]
            # 对应excel中的零件数
            form_out[8] = 1
            form_out[10] = line[9]

            if (line[5] == line[5] and line[6] == line[6]) or (line[5] == line[5] and line[6] != line[6]):
                # 非以号代图件并表中提供规格尺寸
                form_out[0] = line[0]
                form_out[6] = line[5]
                form_out[7] = line[6]
                form_out[5] = line[4]
                self.form_out.append(form_out)
            elif str(line[1]).find('*') != -1:
                # 以号代图件
                form_out[0] = line[0]
                form_out[6] = line[1]
                form_out[7] = 0
                form_out[5] = 0
                self.form_out.append(form_out)
            else:
                omit_value = []
                for i in range(len(line)):
                    omit_value.append(line[i])
                self.omit_value.append(omit_value)


    def to_excel(self):
        df = DataFrame(self.form_out)
        df.to_excel('重整化'+self.addr)

# i = InfoPro('MM-2108  0-0.xlsx')
#
# # print(i.form_out)
# print(i.omit_value)