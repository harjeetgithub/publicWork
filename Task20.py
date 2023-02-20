sum = int(0)
mean = float(0.0)
stdv = float(0.0)
summate = float(0.0)
ele = int(0)
vari = float(0.0)
X = [10, 7, 9, 11, 15, 12, 13, 11, 9, 10]
for i in range(0,len(X)):
    sum = X[i] + sum
mean = sum/10
print(mean)
for j in range(0,len(X)):
    ele = X[j]
    sq = (ele - 10)*(ele - 10)
    summate = summate + sq
summate = summate / 10
stdv = summate ** 0.5
print(stdv)
vari = stdv ** 2
print(vari)
