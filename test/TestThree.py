#!/usr/bin/python
# -*- coding UTF-8 -*-
"""编程第一步"""

# 斐波纳契数列
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b

'end 关键字'
# 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
for x in (1, 2, 3):
    print(x, end=';')