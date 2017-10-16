#!/usr/bin/python
# -*- coding UTF-8 -*-
"""Number中的一些常用运算"""
from random import uniform, shuffle, random, choice

'导入需要的库'
from math import sqrt, fabs, ceil, floor, pi, e

'数学函数'
print(abs(-10.1))  # 返回绝对值
print(fabs(-10))  # 返回绝对值 （浮点型）
print(max(15, 9))  # 求最大值
print(min(15, 9))  # 求最小值
print(ceil(4.1))  # 向上取整
print(floor(4.9))  # 向下取整
print(pow(2, 3))  # 幂运算
print(sqrt(16))  # 求平方根（返回浮点型）
print(round(3.4))  # 返回浮点数四舍五入的值

'随机数函数'
print(random())  # 随机生成下一个实数，它在（0,1）范围内
print(choice(range(10)))  # 随机从零到九挑一个整数
print(uniform(5, 9))  # 随机生成下一个实数，范围在5-9之间
print(round(uniform(5, 9)))  # 随机生成下一个实数，范围在5-9之间，并进行四舍五入处理

'数学常量'
print(pi)  # 数学长量pi（圆周率）
print(e)  # 数学长量e，e即自然数

"""字符串使用"""

'访问字符串中的值'
a = 'Hello World'
b = 'darren573'
print("a[0]", a[0])
print("b[1:5]", b[1:5])
'字符串预算'
print("a+b的值", a + b)
print("a*2的值", a * 2)
print("a[1]的值", a[1])
print("a[1:4]的值", a[1:4])

if ("H" in a):
    print("H在变量a中")
else:
    print("H不在变量a中")

if ("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

'字符串格式化'
print("%s今年%d岁" % ('darren573', 22))  # %s格式化字符串 %d格式化整数 %f格式化浮点数字，可指定小数点后的精度

'字符串内建函数'
str = 'darren'
print(len(str))  # 返回字符串长度
print(str.capitalize())  # capitalize()将字符串的一个字符转换为大写
s = 'DArrEn'
print(s.lower())  # 转换字符串中所有大写为小写

"""列表使用"""
'访问列表中的值'
list1 = ['Google', 'Darren573', 1997, 1995];
list2 = [1, 2, 3, 4, 5, 6, 7];
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

'更新列表'
print("第三个元素为 : ", list1[2])
list1[2] = 2017
print("更新后的第三个元素为 : ", list1[2])

'删除列表元素'
del list1[2]
print("删除第三个元素 : ", list1)

'列表截取与拼接'
print(list1[2])
print(list1[-2])
print(list1[1:])

'嵌套列表'
x = ['a', 'b', 'c']
y = [1, 2, 3]
z = [4.2 + 2j, 4.3 + 2j, 4.4 + 2j]
f = [x, y, z]
print(f)
for q in [1, 2, 3]:
    print(q, end="")  # 迭代
'列表函数&方法'
print(len(list1))
'print(list(seq))'  # 将元组转换为列表
list1.append(2017)
print(list1)

"""字典使用"""
'访问字典中的值'
dict = {"name": "darren573", "age": 22, "sex": "man"}
print("dict['name']", dict['name'])
print("dict['age']", dict['age'])
print("dict['sex']", dict['sex'])

'修改字典中的值'
dict['age'] = 20  # 修改dict中age的值
dict['tel'] = "10086"
print(dict.keys())
print(dict.values())

'删除字典'
del dict['name']
print(dict.keys())
print(dict.values())
"""字典键的特性
    不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住；
    键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行。
"""

'字典内置函数&方法'
print(len(dict))  # 计算字典元素个数，即键的总数。
print(dict.__str__())  # 输出字典，以可打印的字符串表示。
