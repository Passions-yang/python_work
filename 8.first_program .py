#!/usr/bin/python

# 第一个程序
a,b = 0,1
while b < 1000:
    print(b,end=",")
    a,b = b,a + b
'''
    a = 0
    b = 1
    a = b; b = a + b
'''
