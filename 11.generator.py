#!/usr/bin/python3
 
import sys
 
'''
    在 Python 中，使用了 yield 的函数被称为生成器（generator）。

    跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

    在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。

    调用一个生成器函数，返回的是一个迭代器对象。

    以下实例使用 yield 实现斐波那契数列：
'''
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0     # 意味着此处只初始化一次
    while True:
        if (counter > n): 
            return
        yield a     # 遇到生成器是，保存当前变量，并且将a作为迭代器返回，当调用next时，才从此处计息执行
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成

def test():
    while True:
        try:
            print (next(f), end=" ")
        except StopIteration:   #抛出异常
            sys.exit()      # 推出此程序

if 1:
    test()
else:   
    if __name__== "__main__" :
        test()