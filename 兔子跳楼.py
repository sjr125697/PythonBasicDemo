
n=int(input())

def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
if n==1:
    print(1)
elif n==2:
    print(2)
else:
    
    a=(fib(n))[-1]
    b=(fib(n))[-2]
    y=a+b
    print(y)
