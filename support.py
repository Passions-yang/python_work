#!/usr/bin/python3

def my_function(argv):
    print("hello ",argv)
    return

def fib(n):
    a,b = 0,1
    while b < n:
        print(b,end=" ")
        a,b = b,a + b
    print()
    return

if __name__ == '__main__':
    fib(100)
    print('程序自身在运行')  # 当程序自身运行时，走此分支
else:
   print('我来自另一模块')   # 当程序被import时，走此分支