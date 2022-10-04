#!/usr/bin/python3

import sys

# dict 字典
'''
    字典是一种可变容器模型,且可存储任意类型对象
    字典的每个键值 key=>value 使用冒号隔开，每个对之间使用逗号分隔，整个字典使用花括号包含，具体格式如下：
    d = {key1 : value1, key2 : value2, key3 : value3 }
'''
d = {"key1" : "yang", "key2" : "zhi", "key3" : "chao", 1:"123",2:456}
print(d)
print(d[1],d["key1"],'2')  # 从这段代码可以看出，在python中“'”和“"” 符号是一样的，
# 在字典中取数据，如果key是整型，直接写入数字即可，如果以是字符串，使用“'”或“"”符号。
# 在字典中 key值必须是唯一的，value是不唯一的，可以是任意类型
print(type(d),type(d["key1"]),type(d[1]))

# 修改字典
print(d)
d["key2"] = "sun"
print(d)
# 添加字典
d["yang"] = "yan"
print(d)

# 删除字典中某个键值
del d["key3"]
print(d)
# 清空字典树
d.clear()
print(d)
# 删除字典
del d

