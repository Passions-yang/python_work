#!/usr/bin/python3
import sys
import support

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




