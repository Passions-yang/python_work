#!/usr/bin/python3

# python 有两种输出值方式：表达式语句和print()
# 第三种是使用文件对象的write()方法，标准输出文件可以用sys.stdout引用
# 如果想输出多样化： 可以使用str.format()函数来格式化输出
# 如果希望将输出的值转化为字符串，可以使用repr()或str()函数来实现

a = str(1/7)
print(a)

x = 10 * 3.25
y = 200 * 200
s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
print(s)

hello = 'hello, runoob\n'
hellos = repr(hello) # repr 可以转义特殊字符
print(hellos)

# repr() 的参数可以是 Python 的任何对象
a = repr((x, y, ('Google', 'Runoob')))
print(a)


for i in range(1,11):
    print(repr(i).zfill(4), repr(i**2), end=",") # zfill 方法在字符串右边填充0
    print(repr(i**3).rjust(5)) # rjust 配置repr输出属性，字符串靠右，并在左边填充空格
    # repr 方法默认靠左


for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)) # 格式化如左所示

print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))


# 读写文件
# 打开一个文件
f = open("foo.txt", "w")

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

# 关闭打开的文件
f.close()


# 打开一个文件
f = open("foo.txt", "r")

for line in f:
    print(line, end='') # 读取文件每一行

# 关闭打开的文件
f.close()



