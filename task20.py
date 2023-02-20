summate=0
x = [10,7,9,11,15,12,13,11,9,10]
sum=0
n=len(x)
for i in range (len(x)):
    sum=sum+x[i]
    
avrage=sum/n
print("Mean :",avrage)
for j in range(0,len(x)):
    ele = x[j]
    sq=(ele - 10)*(ele - 10)
    summate = summate + sq
summate = summate / 10
stdv = summate ** 0.5
print("stdv :",stdv)
vari = stdv ** 2;
print("vari :",vari)
