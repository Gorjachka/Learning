def fac(n):
    pr=1
    for i in range(1,n+1):
        pr=pr*i
        yield pr


for i in fac(10):
    print(i,end=' ')