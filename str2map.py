#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 20:44
# @Author  : WangYuan
# @Site    : 
# @File    : str2map.py
# @Software: PyCharm
from re import split,match,sub
import re
#
# class Str2map:
#     # 判断输入类型是否为波纹管
#     def __init__(self,str):
#         self.num = 1
#         if match('^b|B[0-9]', str):
#             self.type ='波纹管'
#             bellows = []
#             for i in split('[*-]',str.strip('B').strip('-')):#用re.split可以分割多个分割符
#                 bellows.append(float(i))  #波纹管参数汇总
#             self.parameter = []
#             self.parameter.append((bellows[0] + bellows[-2]) * 3.14)
#             self.parameter.append(2*bellows[1]*bellows[3]+2*90+(bellows[3]*3.14159-2*bellows[3]-1)*bellows[2]/2)
#             self.thickness = bellows[-2]
#             self.num =int( bellows[-3])
#
#             #波纹管重量计算 如果波纹管材料_纵向展开过短将产生dxf文件
#             # if  format_input['parameter'][1] > 1219:
#             #     bellows_weight_1219 = format_input['parameter'][0] * format_input['parameter'][1] * bellows[-2] * 0.00000785 * format_input['sum'] + bellows_weight_1219
#             # elif 950 < format_input['parameter'][1] < 1219 :
#             #     bellows_weight_1219 = format_input['parameter'][0] * 1219 * bellows[-2] * 0.00000785*format_input['sum'] + bellows_weight_1219
#             # elif 700 < format_input['parameter'][1] < 950:
#             #     bellows_weight_1000 = format_input['parameter'][0] * 1000 * bellows[-2] * 0.00000785 * format_input['sum'] + bellows_weight_1000
#             # else:
#             #     DrawCreator(format_input['name'], format_input['type'], format_input['parameter'],format_input['material'],format_input['thickness'],address)
#
#         elif match('[j|J][g|G][0-9]', str) or match('[z|Z][j|J][g|G][0-9]', str) or match('[j|J][l|L][h|H][0-9]', str) or  match('[d|D][h|H][0-9]', str):   #接管类以号代图
#             self.type = '接管'
#             self.parameter = []
#             pipe = []
#             for i in split('[*-]',sub('^[A-Za-z]*','',str).strip('-')):#用re.split可以分割多个分割符
#                 pipe.append(float(i.strip('°')))  #接管参数汇总
#             self.parameter.append((pipe[0] - pipe[1]) * 3.1415926)
#             self.parameter.append(pipe[2])
#             self.thickness = int(pipe[1])
#         elif match('[E|e][B|b]',str) :   #耳板以号代图
#             self.type = '搭板'
#             self.parameter = []
#             plate = []
#             for i in split('[*-]', sub('^[E|e][B|b][0-9]', '', str).strip('-')):  # 用re.split可以分割多个分割符
#                 plate.append(float(i))  # 接管参数汇总
#             self.parameter.append(plate[0])
#             self.parameter.append(plate[1])
#             self.thickness = plate[3]
#         elif match('[D|d][E|e]',str) :          #吊耳以号代图
#             self.type = '搭板'
#             self.parameter = []
#             plate = []
#             for i in split('[*-]', sub('^[D|d][E|e]', '', str).strip('-')):  # 用re.split可以分割多个分割符
#                 plate.append(float(i))  # 接管参数汇总
#             self.parameter.append(plate[0])
#             self.parameter.append(plate[1])
#             self.thickness = int(plate[3])
#         elif match('^[H|h][B|b]',str):          #环板以号代图
#             self.type = '环板'
#             self.parameter = []
#             plate = []
#             for i in split('[*-]', sub('^[H|h][B|b][0-9]', '', str).strip('-')):  # 用re.split可以分割多个分割符
#
#                 plate.append(float(i))  # 接管参数汇总
#             self.parameter.append(plate[0])
#             self.parameter.append(plate[1])
#             self.thickness = int(plate[2])
#         elif match('^[H|h][B|b]',str):          #环板以号代图
#             self.type = '环板'
#             self.parameter = []
#             plate = []
#             for i in split('[*-]', sub('^[H|h][B|b][0-9]', '', str).strip('-')):  # 用re.split可以分割多个分割符
#
#                 plate.append(float(i))  # 接管参数汇总
#             self.parameter.append(plate[0])
#             self.parameter.append(plate[1])
#             self.thickness = int(plate[2])
#         elif match('^[N|n][C|c][0-9]', str) :   #内衬筒类以号代图
#             self.type = '接管'
#             self.parameter = []
#             pipe = []
#             for i in split('[*-]',sub('^[A-Za-z]*','',str).strip('-')):#用re.split可以分割多个分割符
#                 pipe.append(float(i))  #内衬筒参数汇总
#             if len(pipe) == 3:
#                 self.parameter.append((pipe[0] + pipe[-2]) * 3.1415926)
#                 self.parameter.append(pipe[-1])
#             else:
#                 self.parameter.append((pipe[0] + pipe[-2]) * 3.1415926)
#                 self.parameter.append(pipe[-1]+50)
#             self.thickness = int(pipe[-2])
#         elif match('^[W|w][T|t]',str):  #外护套类以号代图
#             self.type = '外护套'
#             self.parameter = []
#             temp = []
#             for i in split('[*-]',sub('[A-Za-z]*','',str).strip('-')):
#                 temp.append(float(i))
#             self.parameter.append((temp[0]+temp[1])*3.14154926)
#             self.parameter.append(temp[2])
#             self.thickness=float(temp[1])
#
#         elif match('^[K|k][W|w][T|t]',str):  #外护套类以号代图
#             self.type = '可拆外护套'
#             self.parameter = []
#             temp = []
#             for i in split('[*-]',sub('[A-Za-z]*','',str).strip('-')):
#                 temp.append(float(i))
#             self.parameter.append((temp[1]+temp[2])*3.14154926/2+60)
#             self.parameter.append(temp[3])
#             self.thickness=float(temp[2])
#             self.num=2
#         else:
#             print("该以号代图未收录")
#

class Str2map:
    # 判断输入类型是否为波纹管
    def __init__(self,str):
        self.num = 1
        if match('^b|B[0-9]', str):
            self.type ='波纹管'
            bellows = []
            for i in split('[*-]',str.strip('B').strip('-')):#用re.split可以分割多个分割符
                bellows.append(float(i))  #波纹管参数汇总
            self.parameter = []
            self.parameter.append((bellows[0] + bellows[-2]) * 3.14)
            self.parameter.append(2*bellows[1]*bellows[3]+2*90+(bellows[3]*3.14159-2*bellows[3]-1)*bellows[2]/2)
            self.thickness = bellows[-2]
            self.num =int( bellows[-3])
            return

        elif match('^[J|j][G|g]',str) or match('^[Z|z][J|j][G|g]',str) or match('^[J|j][L|l][H|h]',str) or match('^[D|d][H|h]',str) :   #接管、中间接管、剪力环以号代图
            self.type='接管'
            self.parameter={}
            temp=[]
            for i in re.findall('\d+\.\d+|\d+',str):
                temp.append(float(i))
            if(re.findall('[N|n]',str)):
                self.parameter.update({'w': (temp[0] + temp[1]) * 3.1415926})
            else:
                self.parameter.update({'w': (temp[0] - temp[1]) * 3.1415926})
            self.parameter.update({'l': temp[2]})
            self.thickness=float(temp[1])
            return

        elif match('[E|e][B|b]',str) :   #耳板以号代图
            self.type = '耳板'
            self.parameter = {}
            temp = []
            for i in re.findall('\d+\.\d+|\d+',str):
                temp.append(float(i))  # 接管参数汇总
            self.parameter.update({'w': temp[1]})
            self.parameter.update({'l': temp[2]})
            self.thickness = float(temp[4])
            return

        elif match('[D|d][E|e]',str) :          #吊耳以号代图
            self.type = '吊耳'
            self.parameter = {}
            temp = []
            for i in re.findall('\d+\.\d+|\d+', str):
                temp.append(float(i))  # 接管参数汇总
            self.parameter.update({'w':temp[0]})
            self.parameter.update({'l': temp[1]})
            self.thickness = float(temp[3])
            return

        elif match('^[H|h][B|b]',str):          #环板以号代图
            self.type = '环板'
            self.parameter = {}
            temp = []
            for i in re.findall('\d+\.\d+|\d+', str):
                temp.append(float(i))
            self.parameter.update({'od':temp[1]})
            self.parameter.update({'id':temp[2]})
            self.thickness = float(temp[3])
            return

        elif match('^[N|n][C|c]', str) :   #内衬筒类以号代图
            self.type = '内衬筒'
            self.parameter = {}
            temp = []
            for i in  re.findall('\d+\.\d+|\d+', str):
                temp.append(float(i))
            if(len(re.findall('\*',str))==1):
                self.parameter.update({'w':(temp[0]-temp[1])*3.1415926})
                self.parameter.update({'l':temp[2]})
                self.thickness=float(temp[1])
            else:
                if((temp[0]-temp[1])/2>30):
                    self.parameter.update({'l': temp[3] + 10})
                else:
                    self.parameter.update({'l': temp[3] + 5})
                self.parameter.update({'w': (temp[1]-temp[2]) * 3.1415926})
                self.thickness=float(temp[2])
            return
        elif match('^[W|w][T|t]',str):  #外护套类以号代图
            self.type = '外护套'
            self.parameter = {}
            temp = []
            for i in re.findall('\d+\.\d+|\d+', str):
                temp.append(float(i))
            self.parameter.update({'w':(temp[0]-temp[1])*3.1415926})
            self.parameter.update({'l':temp[2]})
            self.thickness=float(temp[1])
            return
        elif match('^[K|k][W|w][T|t]',str):  #可拆卸外护套类以号代图
            self.type = '可拆外护套'
            self.parameter = {}
            temp = []
            for i in re.findall('\d+\.\d+|\d+', str):
                temp.append(float(i))
            if temp[0]==1:
                self.parameter.update({'w':(temp[1]+temp[2])*3.14154926/2+60})
            else:
                self.parameter.update({'w':(temp[1] + temp[2]) * 3.14154926 / 2})
            self.parameter.update({'l':temp[3]})
            self.thickness=float(temp[2])
            self.num=2
            return
        elif match('^[J|j]|[B|b]',str):
            self.type='铰链板'
            self.parameter={}
            temp = []
            for i in re.findall('\d+\.\d+|\d+', str):
                temp.append(float(i))
            self.parameter.update({'w': temp[0]})
            self.parameter.update({'l': temp[1]})
            self.thickness = float(temp[2])
        else:
            errorInfo=str+"该以号代图未收录"
            print(str+errorInfo)
            raise Networkerror(errorInfo)

class Networkerror(BaseException):
  def __init__(self, arg):
      self.arg = arg