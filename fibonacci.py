def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
for i in range(6):
    print(fibo(i),end=" ")
