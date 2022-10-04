# !/usr/bin/python3
import sys

count = 1
var = 1
while var == 1:
    print("进入死循环了",count)
    count += 1
    if count > 10:
        break
else:
    print("推出循环了")


while var:      # 条件不成立时，进入else
    print("死循环")
    var = 0
else:
    print("tuichule")
    
var = 1    
while var:
    print("死循环")
    break   # break 退出之后，由于不是condition不成立，所以并不会进入else分支
else:
    print("tuichule")
    

# for 循环
'''
    for <variable> in <sequence>:
        <statements>
    else:
        <statements>
'''

languages = ["C", "C++", "Perl", "Python"] 
for x in languages:
    if x == "C++":
        print("languages is ",x)
        continue
    print (x)
else:
    print("for 循环退出")
    
# range()函数
# 如果需要遍历数字序列，使用range函数
for i in range(10):
    print(i)
for i in range(100,103):
    print(i)
    
for i in range(-10, -100, -30) :  # 输出一个以 -10 为起始数据，-30为间隔的等差队列
    print(i)

for i in range(10, 100, 20) : # 输出一个以 10 为起始数据，20为间隔的等差队列
    print(i)
    
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
print(a)
print(len(a))

for i in range(len(a)):
    print(i,a[i])
# 输出结果如下所示：
'''
    0 Google
    1 Baidu
    2 Runoob
    3 Taobao
    4 QQ
'''
# 使用range创建列表
a = list(range(10)) # list 表示声明创建一个列表
print(list)     # 打印list类型，list是python的一种数据类型

print(a)
for i in a:
    print(i)
