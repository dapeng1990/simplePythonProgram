# 斐波那契数列


# 简单的打印数列中各元素
print("fab函数----简单的打印数列中各元素")
def fab(max):
    n,a,b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
        
fab(10)


# 直接生成list的斐波那契数列
def fabList(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L

print("fabList函数----直接生成list的斐波那契数列")
for n in fabList(10):
    print(n)


#iterable迭代的斐波那契数列
print("Fab类----iterable迭代的斐波那契数列")
class Fab(object):      #object,o小写，与Java不一样
    def __init__(self,max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1
        
    def __iter__(self):   #从python3开始，要使用__iter__
        return self
        
    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()
        
for n in Fab(5):
    print(n)


#使用yield的斐波那契数列
#yield 的作用就是把一个函数变成一个 generator(生成器)，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield
#注意区分 fab 和 fab(5)，fab 是一个 generator function，而 fab(5) 是调用 fab 返回的一个 generator，好比类的定义和类的实例的区别
print("fab_yield----使用yield的斐波那契数列")
def fab_yield(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b;
        a, b = b, a + b
        n = n + 1
        
for n in fab_yield(6):
    print(n)



























