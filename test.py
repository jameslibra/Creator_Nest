
import re
print(re.findall('\d+\.\d+|\d+','JB1020*550*4.5-121*180+.10'))
print(re.findall('\d+\.\d+|\d+','67.5°'))
format={}
format.update({1:1})
print(format[1])
print(str(format))
class Networkerror(BaseException):
  def __init__(self, arg):
      self.arg = arg
try:
    str='Bad hostname'
    raise Networkerror(str)
except BaseException as e:
    print(e.arg)