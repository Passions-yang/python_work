import sys #导入sys包

print("==========================")
print("命令行解析")

for i in sys.argv:
    print(i)
print("python path: ",sys.path)
print(sys.base_exec_prefix,sys.executable)
print(sys.modules)