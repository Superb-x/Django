'''快速排序算法实现'''
import random
import time
import sys
arr = []
s = time.time()
for x in range(10):
    arr.append(random.randint(0, 100))

e = time.time()
print(arr)
print(e - s)
obj = {
    'a': '刘祥麟',
    'b': 'liuxianglin',
    'c': 'liuxianglinaaaaaaa'
}
print(obj['a'])

# sum operation
def fact(x):
    return x > 1 and x * fact(x - 1) or 1
print(fact(6))

# use the lambda function
f = lambda x: x and x * f(x - 1) or 1
print(f(6))