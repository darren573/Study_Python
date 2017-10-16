#!/usr/bin/python
# -*- coding UTF-8 -*-
print("Hello World")
days = ['Monday', 'Tuesday', '星期三', '星期四', '星期五', '星期六', 'sunday']
print(days)
# 第一个注释
'total = item_one + \
         item_two + \
         item_three'
# 第二个注释
word = 'word'
sentence = "这是一个句子"
paragraph = """这是一个段落"""
print(word);
print(sentence);
print(paragraph)

x = "a"
y = "b"
# 输出换行
print(x)
print(y)

print('----------')
# 不换行输出--2.X版本
print(x),
print(y),
# 第二种不换行输出--2.X版本
print(x), print(y)
# 不换行输出--3.X版本
print(x, end="")
print(y, end="")
print()
"""3.x中的标准数据类型之Number"""
a = 111
b = 111.1
c = 4 + 3j
d = True
# 使用isinstance判断变量的类型
print(isinstance(a, int))
print(isinstance(b, float))
print(isinstance(c, complex))  # complex 代表复数
print(isinstance(d, bool))  # bool 代表Boolean值

# 数值运算
print(5 + 4)  # 加法
print(5.3 - 2)  # 减法
print(5 * 9)  # 乘法
print(4 / 16)  # 除法，得到一个浮点数
print(4 // 16)  # 除法，得到一个整数
print(22 % 3)  # 取余
print(3 ** 6)  # 乘方

"""3.x中的标准数据类型之String"""
str = 'darren'
print(str)
# 截取输出
print(str[0:1])
print(str[2:6])
# 连续输出两次
print(str * 2)
# 连接字符串
print(str + "573")

# 反斜杠，转义字符
print('Ru\noob')
# 反斜杠发生转义
print(r'Ru\noob')
"""3.x中的标准数据类型之List列表"""
list = ['abcd', 1234, 'darren573', 22.3]
tinylist = [678, '菜鸡的学习']
print(list)
print(list[0:1])
print(list[2:])
print(tinylist)
print(tinylist * 2)
print(list + tinylist)
# 3.x中的标准数据类型之Tuple元组
tuple = ('abcd', 1234, 'darren573', 22.3)
tinytuple = (678, '菜鸡的学习')
print(tuple)
print(tuple[0:1])
print(tuple[2:])
print(tinytuple)
print(tinytuple * 2)
print(tuple + tinytuple)
# 列表list和元组tuple的区别
listtest = [1, 2, 3, 4, 5, 6]
print(listtest)
listtest[0] = 19
listtest[1:3] = [17, 18, 19]
print(listtest)
'元组tuple中的元素不能改变'
"""3.x中的标准数据类型之Set集合"""
student = {'二狗', '狗剩', '二娃', '二妮'}
if ('二娃' in student):
    print('二娃在Set集合中')
else:
    print('二娃不在Set集合中')
# 使用Set集合进行除重
a = set('abababababcdcdcdcd')
print(a)
b = set('alacazam')
print(b)
print(a - b)  # a和b的差集
print(a | b)  # a和b的并集
print(a ^ b)  # a和b中不同时存在的元素
print(a & b)  # a和b的交集
"""3.x中的标准数据类型之Dictionary字典"""
# 键值对的方式存储数据
dicts = {}
dicts['one'] = "first"
dicts['two'] = "second"
tinydict = {'name': 'darren573', 'age': 22, 'sex': 'man'}
print(dicts['one'])
print(tinydict)
print(tinydict.keys())  # 输出所有的key
print(tinydict.values())  # 输出所有的值