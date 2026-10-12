def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2) #1st call returns lambda a:a*n n=2, lambda remembers

print(mydoubler(11)) # 2nd call , a-11, n-2