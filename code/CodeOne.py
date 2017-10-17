#!/usr/bin/python
# -*- coding UTF-8 -*-
'编程'
from math import sqrt

import math

"""
age = int(input("请输入你家狗狗的年龄："))
print("")
if age < 0:
    print("Are you kidding me ?!")
elif age == 1:
    print("相当于人的14岁")
elif age == 2:
    print("相当于人的22岁")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄：", human)
### 退出提示
input("点击enter键退出")
"""

# 数字猜谜游戏
"""
number = 7
guess = -1
print("数字猜谜游戏")
while guess != number:
    guess = int(input("请输入你猜的数字："))
    if guess == number:
        print("恭喜你答对了！")
        ### 退出提示
        input("点击enter键退出")
    elif guess < number:
        print("猜的数字太小了...")
    else:
        print("猜的数字太大了...")

"""
# Another Test
"""
num = int(input("请输入数字："))
if num % 2 == 0:
    if num % 3 == 0:
        print("你输入的数字可以整除2和3")
    else:
        print("你输入的数字可以整除2，但不能整除3")
else:
    if num % 3 == 0:
        print("你输入的数字可以整除3，但不能整除2")
    else:
        print("你输入的数字不能整除2和3")
"""
# 程序题
for i in range(100000):
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if (x * x == i + 100) and (y * y == i + 268):
        print(i)
