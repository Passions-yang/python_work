#!/usr/bin/python3
import sys
import support
from support import fib

'''
    1、import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
    2、sys.argv 是一个包含命令行参数的列表。
    3、sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。
'''
# import 语句


support.my_function("yangzhichao nishi zhu")
# 使时只需要导入即可
print('\n\nPython 路径为：', sys.path, '\n')
#if __name__ == "__main__":

# from modulename import name 将modulename模块中的函数或者变量导入到此命名空间，可以直接调用
'''
    from modname import name1[, name2[, ... nameN]]
    例如：
        from support import fib
    注：
        把一个模块的所有内容全都导入到当前的命名空间也是可行的
        from sys import *
'''
fib(100)

# 深入模块
'''
    import sys 这种方式，是将sys模块的所有全局变量和函数放在函数表中，
        当作全局符号表来使用，使用时必须使用modname.itemname来使用，所以
'''

a = dir(support)  # 内置函数可以查看模块内定义的所有名称
print(a)

