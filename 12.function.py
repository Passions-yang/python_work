#!/usr/bin/python3

# 函数
'''
    * 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
    * 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
    * 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
    * 函数内容以冒号 : 起始，并且缩进。
    * return [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。
'''

def test(n):
    if n < 10:
        print("n < 10")
    else:
        print("n >= 10")
        
test(10)

def area(width, height):
    return width * height

print(area(10,6))   # 计算长方形面积

# 参数传递
'''
    可更改(mutable)与不可更改(immutable)对象
        在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

        不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。

        可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

    python 函数的参数传递：

        不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。

        可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

        python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
'''


def change(a):
    print(id(a))   # 指向的是同一个对象
    a=10
    print(id(a))   # 一个新对象
 
a = 1
print(id(a))
change(a)
print(id(a))
print(a)

# 可写函数说明
def changeme(listme):
    print(id(listme))
    print(id(listme[1]))    # 打印原来列表中内存
    listme[1] = 50      # 更改列表值
    print(id(listme[1]))    # 再次打印，可以看出列表中数据内存被释放，知识重新申请内存了
    print(id(listme))
    listme.append(1)
    listme.append([2,3,4,5,6])



listme = [10,20,30]
print(listme)
changeme(listme)
print(listme)
print(listme[4])


#可写函数说明
def printme( str ):
   "打印任何传入的字符串"
   print (str)
   return
 
# 调用 printme 函数，不加参数会报错
#printme()   # 报错，因为必须传入参数
printme("孙燕你是猪？") 


#可写函数说明
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="runoob" )  # 从此处可以看出，默认参数可以没有顺序
print ("------------------------")
printinfo( name="runoob" )
printinfo("yangzhichao")
printinfo(47,"yangzhichao")  # 如果不指定赋值对象，那么赋值使用的是默认顺序


# 不定长参数

'''
    def functionname([formal_args,] *var_args_tuple ):
        "函数_文档字符串"
    function_suite
    return [expression]
    注：
        加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。元组是不可变参数
    所以参数传递之后，在函数中不可更改
    
    def functionname([formal_args,] **var_args_dict ):
       "函数_文档字符串"
    function_suite
    return [expression]
    注：
        加了两个星号 ** 的参数会以字典的形式导入，字典是可变参数，传递参数之后，可以通过函数进行改变
   
'''

# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
 
# 调用printinfo 函数
printinfo( 100)
printinfo( 70, 60, 50 )
printinfo( 70, 60, 50 ,70, 60, 50 ,70, 60, 50 ,70, 60, 50 ,70, 60, 50 ,70, 60, 50 ,70, 60, 50 )

def printinfo( arg1, *vartuple ):
    "打印任何传入的参数"
    print("输出: ")
    print (arg1)
    for var in vartuple:
        print (var)
    return
 
# 调用printinfo 函数
printinfo( 10 )
printinfo( 70, 60, 50 )


def printinfo( arg1, **vardict ):
    "打印任何传入的参数"
    print ("输出: ")
    print (arg1)
    print (vardict)
    vardict["a"] = 3
    print(vardict)
 
# 调用printinfo 函数
printinfo(1, a=2,b=3)

# 匿名函数
'''
Python 使用 lambda 来创建匿名函数。

所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

    * lambda 只是一个表达式，函数体比 def 简单很多。
    * lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
    * lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
    * 虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率
'''
# 语法如下：
'''
    lambda [arg1 [,arg2,.....argn]]:expression
'''

x = lambda a : a + 10
print(x(5))



sum = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))

"""
    我们可以将匿名函数封装在一个函数内，这样可以使用同样的代码来创建多个匿名函数。

    以下实例将匿名函数封装在 myfunc 函数中，通过传入不同的参数来创建不同的匿名函数：
"""

def myfunc(n):
      return lambda a : a * n
 
mydoubler = myfunc(2)
mytripler = myfunc(3)
 
print(mydoubler(11))
print(mytripler(11))




