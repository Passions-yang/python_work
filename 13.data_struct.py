#!/usr/bin/python3

# 列表提供了丰富的方法，合理使用方法，可以将列表当错堆栈，队列等使用。
# 当作堆栈使用
a = [1,2,4,5,6,7,8]
a.append(20)
print(a)
a.append(100)
print(a)
a.pop();
print(a)
a.pop();
a.pop();
a.pop();
a.pop();
print(a)



# 列表推导式
vec = [2, 4, 6]
a = [3*x for x in vec]
print(a)

a = [3*x for x in vec if  x > 5]
print(a)


freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
strb = [weapon.strip() for weapon in freshfruit]
print(strb)
# strip() 字符串处理函数，去掉字符串头尾的多余字符
stra = "   yang sun \n   "
stra.strip() # str变量无法更改，所以使用print(stra) 打印和原先一样，必须使用下面方法，可以重新生成字符串对象
strac = stra.strip() 
print(stra)
print(strac)

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
a = [x*y for x in vec1 for y in vec2]
print(a)


vec1 = [2, 4, 6,16]
vec2 = [4, 3, -9,15]
a = [vec1[x]*vec2[x] for x in range(len(vec1))]
print(a)

vec1 = [2, 4, 6,16]
vec2 = [4, 3, -9,15]

a = [[vec1[x],vec2[x]] for x in range(len(vec1))]
print(a)

matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]

a = [[x[i] for x in matrix]  for i in range(len(matrix))]
print(a)
'''
    range(len(matrix)) == 3  ===> i 从0 --> 3
    i == 0 时， for x in matrix 进行循环，x分别等于[1, 2, 3, 4]，[5, 6, 7, 8],[9, 10, 11, 12]，
        取第一列的元素，x[i],所以组成新的矩阵为 [1,5,9]
        
'''
# 第二种方法
transposed = []
for i in range(len(matrix)):
    transposed.append([row[i] for row in matrix])
print(transposed)

# 第三种方法
transposed = []
for i in range(len(matrix)):
    transposed_row = []
    for x in matrix:
        transposed_row.append(x[i])
    transposed.append(transposed_row)
print(transposed)

# 综上三种方法，可以看出推导式多么强大

# del 语句
'''
    使用 del 语句可以从一个列表中根据索引来删除一个元素，而不是值来删除元素。这与使用 pop() 返回一个值不同。
    可以用 del 语句从列表中删除一个切割，或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）。例如：
'''
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[3]
print(a)
del a[2:4]
print(a)
# del a # 不能使用这种删除方式，必须使用del a[:] 这种方式
print(a)
del a[:]    # 删除列表a中所有元素
print(a)

#  集合
'''
    集合是一个无序不重复元素的集，基本功能包括关系测试和消除重复元素，使用大括号创建，空集合必须使用set()创建。
'''

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # 可以看出，创建的时候自动删除了重复项
a = 'orange' in basket  
print(a) # 打印为true

a = set('abracadabra')
b = set('alacazam')

c = a - b
print(c)
c = a | b
print(c)
print(a & b)


a = {x for x in "abcdefgshhhhaj" if x not in "abc"}
print(a)

#  字典
'''
    序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，
    关键字必须是唯一的，可以是数字或者字符串，理解字典的最佳方式是把他看做
    无需的键值对集合。，使用大括号来创建字典，创建空字典使用{}
'''
a = {"yang":"sun","zhichao":"yan","age_yang":28,"age_sun":29}
print(a)
a["age_yang"] = 30
print(a)

del a["age_sun"]
print(a)

c = "age_yang" in a
print(c)

# 字典类型遍历技巧
a = {"yang":"sun","zhichao":"yan","age_yang":28,"age_sun":29}
for k,v in a.items():
    print(k,v)
 
for i in reversed(range(1, 10, 2)):
    print(i)
basket = {'apple', 'orange', 'pear','banana'}  # 创建一个集合set
basket = ['apple', 'orange', 'pear','banana']  # 创建一个字典
print(type(basket))
dicta = {i : x for x in basket for i in range(len(basket))} # 根据集合创建一个字典
print(dicta) 


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):  # 使用sorted 来排序，输出一个排序列表
    print(f)







    












