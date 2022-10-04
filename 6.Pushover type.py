#!/usr/bin/python3
# 各种数据结构的推导式
'''
    * 列表(list)推导式
    * 字典(dict)推导式
    * 集合(set)推导式
    * 元组(tuple)推导式
'''
# 列表(list)推导式
'''
    [表达式 for 变量 in 列表] 
    [out_exp_res for out_exp in input_list]

    或者 

    [表达式 for 变量 in 列表 if 条件]
    [out_exp_res for out_exp in input_list if condition]
    
    out_exp_res：列表生成元素表达式，可以是有返回值的函数。
    for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中。
    if condition：条件语句，可以过滤列表中不符合条件的值。
'''

names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper() for name in names if len(name)>3]  
# 从names中拿到每一个元素,放入name,根据条件if len(name)>3,传入列表生成表达式name.upper(),将每一个字符串类型转换为大写，并且赋值给new_names
print(new_names)

multiples = [i for i in range(50) if i % 2 == 0]    
# 通过range函数，便利每一个数据，将数据放入变量i中，根据条件 if i % 2 == 0，刷选数字，将帅选到的数字复制给列表表达式i,把每一个i复制给multiples
print(multiples)


# 字典推导式
'''
    字典推导基本格式：

    { key_expr: value_expr for value in collection }
    或
    { key_expr: value_expr for value in collection if condition }
'''
listdemo = ['Google','Runoob', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key:len(key) for key in listdemo}
print(newdict)

list_int = [10,2,3,4,5,6,7,8]
new_int = {i:i*i for i in list_int}
print(new_int)

# 集合推导式
'''
    集合推导式基本格式：

    { expression for item in Sequence }
    或
    { expression for item in Sequence if conditional }
'''

list_int = [1,2,3]
setnew = {i**4 for i in list_int}  # 在 python中一个"*"表示，乘，两个"**"表示次方，例如：3*2 == 4  3**2 == 9
print(setnew)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
type(a)

# 元组推导式（生成器表达式）
'''
    元组推导式可以利用 range 区间、元组、列表、字典和集合等数据类型，快速生成一个满足指定需求的元组。

    元组推导式基本格式：

    (expression for item in Sequence )
    或
    (expression for item in Sequence if conditional )
    元组推导式和列表推导式的用法也完全相同，只是元组推导式是用 () 圆括号将各部分括起来，而列表推导式用的是中括号 []，另外元组推导式返回的结果是一个生成器对象。

    例如，我们可以使用下面的代码生成一个包含数字 1~9 的元组：
'''
a = (x for x in range(1,10))
print(a)  # 返回的是生成器对象
b = tuple(a)       # 使用 tuple() 函数，可以直接将生成器对象转换成元组
print(b)

# 数组和元组之间的区别是什么
'''
    区别：
        数组内容是可以被修改的，而元组内容是只读的。另外，元组可以被哈希，比如作为字典的关键字。
        数组在python中叫做列表。列表可以修改，如果元组中仅有一个元素，则要在元素后加上逗号。元组和列表的查询方式一样。元组只可读不可修改，如果程序中的数据不允许修改可用元组。
'''