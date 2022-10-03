import sys
from sys import argv,path #将sys包中成员变量导入 argv,path

for arg in argv: #由于已经将成员变量argv和path导入，所以可以将sys.argv 写成 argv
    print(arg)
    
print(path) # path == sys.path
str = sys.executable
print(str)
