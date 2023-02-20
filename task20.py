import math

l=int(input("Enter number of elements "))
a=[]
b=[]
c=[]
x=0
for i in range(l):
    n=int(input())
    a.append(n)

for i in range(l):
    x=x+a[i]

mean=x/l
print("Mean is",mean)

for i in a:
    b.append(i-mean)
    
for i in b:
    c.append(i**2)



f=sum(c)/l
sd=math.sqrt(f)
print("Standard Deviation is",sd)
v=sd**2
print("Variance is",v)
