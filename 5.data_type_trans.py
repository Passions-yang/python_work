#!/usr/bin/python3

import sys
 
num_int= 123
num_flo = 1.23

num_new = num_int + num_flo # 隐式的类型转换

print(num_int,type(num_int))
print(num_flo,type(num_flo))
print(num_new,type(num_new))

x = 2
y = 3.5
z = int(y)  # 显式类型转换，将float y = 3.6 转换为 int 型3
print(x,y,z)

w = float(z) # 将整型 z 转换为 float类型
print(w)

num_str = "456"
print("num_str type is : ",type(num_str))
num_str_int = int(num_str)
print("num_str_int type is : ",type(num_str_int)," value :",num_str_int)

int_to_str = str(num_str_int)  # 将整型转换为字符串类型
print("int_to_str is type : ",type(int_to_str),"string : ",int_to_str)



