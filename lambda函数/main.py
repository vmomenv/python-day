#lambda匿名函数
#语法格式：lambda arguments:expression
#lambda 是定义lambda函数；argument是参数列表；expression是表达式，返回计算结果

#无参数lambda

f=lambda :"hello world"

print(f())

# 创建匿名函数，设置一个参数a，函数计算参数a+10

x=lambda a:a+10
print(x(5))

#等价于
def x(a):
    return a+10
print(x(5))

#多个参数
x=lambda a,b:a+b
print(x(5,6))

#############################################################################
print("####lambda与map函数使用####")
#lambda函数 与内置函一起使用
#map函数用法: 将一个函数应用到迭代对象（列表元组等），返回一个迭代器
#map(function, iterable) function 函数；iterable 迭代对象
number=[1,2,3,4,5,6,7,8,9,10]
def square(x):
    return x**2

print(list(map(square,number)))#list函数将迭代对象转换为列表



square2 = list(map(lambda x:x**2, number))
print(square2)

#############################################################################
print("####lambda与filter函数使用####")
#filter函数用法: 将一个函数应用到迭代对象（列表元组等），返回一个迭代器,如果函数返回true,则元素保留，否则过滤
#以下是输出偶数
number=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x:x%2==0,number)))
