import sys

count = 100     #整型
miles = 100.0   # 浮点型
name = "name"   #字符串类型

print(count)
print(miles)
print(name)

a = b = c = 100
print(a,b,c)
x,y,z = 100,300.0,"yangzhichao"
print(x,y,z)

# python 标准数据类型

'''
    Number 数字
    string 字符串
    list 列表
    tupple 元组
    set 集合
    dictionary 字典
    不可变数据类型： number, string, tupple
    可变数据： list,set,dictionary 
'''
# 数字类型：
'''
    python3 支持类型： int,float,bool,complex复数
'''
print(type(a),type(b),type(c))
a,b,c,d = 20,5.5,True,4+3j
print(type(a),type(b),type(c),type(d))

isinstance(a,int)   # 判断变量a是int吗？
isinstance(c,set)

