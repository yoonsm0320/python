def fibo(n):
    if n==0 or n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
for i in range(16):
    print(f"fibo({i:2}) = {fibo(i):4}")