def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        print("a=",a," b=", b)# Get first 100 Fibonacci numbers
gen = fibonacci()
for i in range(100):
    print(next(gen))