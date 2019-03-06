def sort(a,b,c):
    if a>b:
        a,b=b,a
        # print (a,b)
    if b>c:
        b,c=c,b
    if a>b:
        a,b=b,a
    return a,b,c

x=input('first number :')
y=input('second number :')
z=input('third number :')
print(sort(x,y,z))