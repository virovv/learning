from math import *
num = int(input())

def  TrPa(n):
    l = []
    for i in range(n+1):
        s = [1]
        for j in range(1, i+1):
            
            s.append(int(factorial(i) / ((factorial(j) * factorial(i - j)))))
        l.append(s)

    return print(l[n])

TrPa(num)