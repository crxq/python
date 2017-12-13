# -*- coding: utf-8 -*-
#水仙花函数
input('请输入回车进入下一题')
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            if i*100+j*10+k==i**3+j**3+k**3:
                a = i ** 3 + j ** 3 + k ** 3
                print(a)


#斐波那契数列
input('请输入回车进入下一题')
def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))

for i in range(9):
    print(str(recur_fibo(i)),end=',')

#递归函数
input('请输入回车进入下一题')
def digui(n):
    if n==1:
        return n
    else:
        return n*digui(n-1)

num=int(input('请输入一个数：'))
print(digui(num))

#尾递归
input('请输入回车进入下一题')
def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)
print(fact(int(input('请输入一个数：'))))
