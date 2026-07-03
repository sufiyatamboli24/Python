def fabonacci(n):
    a,b=0,1
    series=[]
    for i in range(n):
       series.append(a)
       c=a+b
       a=b
       b=c
    return series   