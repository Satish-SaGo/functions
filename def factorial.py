def factorial(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s
n=int(input())
g=factorial(n)
print(g)
