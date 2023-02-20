s = int(0)
m = float(0.0)
SD = float(0.0)
sum= float(0.0)
ele = int(0)
v = float(0.0)
X = [10, 7, 9, 11, 15, 12, 13, 11, 9, 10]
for i in range(0,len(X)):
    s = X[i] + s
m = s/10
print(m)
for j in range(0,len(X)):
    ele = X[j]
    sq = (ele - 10)*(ele - 10)
    sum= sum+ sq
sum= sum/ 10
SD = sum** 0.5
print(SD)
v = SD **2
print(v)

