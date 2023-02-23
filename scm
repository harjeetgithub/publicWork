x =[10,7,9,11,15,12,13,11,9,10]
mean = sum(x)/len(x)
print("the mean of the numbers is:",mean)
difference = (y -  mean for y in x)
squared_diff = [d**2 for d in difference]
sum_squared_diff = sum(squared_diff)
n =len(x)
variance = sum_squared_diff/(n-1)
std_dev = variance**0.5
print("the standard deviation of the x is :", std_dev)
variance_diff = [(num - mean)**2 for num in x]
variance_squ_diff = sum(variance_diff)
variance = variance_squ_diff/(len(x)-1)
print("variance of number is:",variance)

