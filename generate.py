#生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
print(list(range(1,11)))

print("方法一,循环生成[1x1, 2x2, 3x3, ..., 10x10] ")
L=[]
for x in range(1,11):
    L.append(x*x)
print(L)

print("方法二，列表生成式生成[1x1, 2x2, 3x3, ..., 10x10]")
print([x * x for x in range(1,11)])

print("列表生成式生成[1x1, 2x2, 3x3, ..., 10x10]，仅保留偶数的平方")

print([x * x for x in range(1,11) if x % 2 == 0])

print("列表生成式 两层循环，生成全排列 [m + n for m in 'ABC' for n in 'XYZ']")
print([m + n for m in 'ABC' for n in 'XYZ'])

print("列出当前目录下的所有文件和目录名 [d for d in os.listdir('.')]")
import os
print([d for d in os.listdir('.')])



print("列表生成式也可以使用两个变量来生成list")
aa = {'x':'A','y':'B','z':'C'}
print([k + '=' + v for k,v in aa.items()])

print("把一个list中所有的字符串变成小写")
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])


print("在Python中，这种一边循环一边计算的机制，称为生成器：generator")
print("创建一个generator方法一，把一个列表生成式的[]改成(),g = (x * x for x in range(10))")
g = (x * x for x in range(10))
print(g)


print("如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator")
















