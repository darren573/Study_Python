#!/usr/bin/python
# -*- coding UTF-8 -*-

"""以下实例
x 为 0-99 取一个数,y 为 0-199 取一个数,
如果 x>y 则输出 x，
如果 x 等于 y 则输出 x+y，
否则输出y"""
import random

x = random.choice(range(100))
y = random.choice(range(200))
if x > y:
    print('x', x)
elif x == y:
    print('x+y', x + y)
else:
    print('y', y)
