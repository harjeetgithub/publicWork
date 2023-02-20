def variance(data):
     n = len(data)
     mean = sum(data) / n
     deviations = [(x - mean) ** 2 for x in data]
     variance = sum(deviations) / n
     return variance


variance([10,7,9,11,15,12,13,11,9,10])






numb = [10,7,9,11,15,12,13,11,9,10]
no = len(numb)
summ = sum(numb)
mean = summ / no
print("The mean or average of all these numbers (", numb, ") is", str(mean))
