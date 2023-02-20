import math

a=int(input("Enter number of elements"))
l1=[]
l2=[]
l3=[]
x=0
for i in range(a):
    n=int(input())
    l1.append(n)

print(l1)
for i in range(a):
    x=x+l1[i]

mean=x/a
print("Mean is",mean)

for i in l1:
    l2.append(i-mean)
    
for i in l2:
    l3.append(i**2)



p=sum(l3)/a
sd=math.sqrt(p)
print("Standard Deviation",sd)
v=sd**2
print("Variance",v)
