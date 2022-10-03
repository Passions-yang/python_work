#!/usr/bin/python3
import sys
# 第一个注释
print("hello world") # 第二注释

'''
    第三行注释
    第四行注释
'''
print("yangzhichao nihao ");
"""
    上图是换行打印
"""
if True:
    print ("true")
else:
    print("false")
    print("123")
TEST= " this " "is " "string"
print(TEST)
print(TEST[0])
print(TEST[-1])
print(TEST[2])
print(TEST[10])

print(TEST[2:5])
print(TEST[2:])

print(TEST[2:-2])
print(TEST[2:-2] + " yangzhichao")

x = "yangzhichao"
sys.stdout.write(x + '\n')
sys.stdout.write(" hi \n") 

i = 18
if i > 20:
    print("i > 25")
elif i > 10:
    print("10 < i < 20")
else:
    print("i < 10")
    
print(i)    #换行输出
print(i, end=" ") # 不换行输出
print(i, end=" ") # 不换行输出