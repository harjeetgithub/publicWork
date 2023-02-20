import math 
n=int(input("enter elements"))
l=[]
l1=[]
l2=[]
x=0
for i in range(n):
    a=int(input())
    l.append(a)

print(l)

for i in range(a):
    x=x+l[i]

b=x/a
print(b)

for i in l:
    l1.append(i-b)

print(l1)

for i in l1:
    l2.append(i**2)

print(l2)

p=sum(l2)/a
sd=math.sqrt(p)
print("standard deviation",sd)
v=sd**2
print("variance",v)
