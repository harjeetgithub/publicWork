import math
#SD
dataset = [10,7,9,11,15,12,13,11,9,10]

sm=0
for i in range(len(dataset)):
   sm+=dataset[i]
   mean = sm/len(dataset)

deviation_sum = 0
for i in range(len(dataset)):
   deviation_sum+=(dataset[i]- mean)**2
   psd = math.sqrt((deviation_sum)/len(dataset))

ssd = math.sqrt((deviation_sum)/len(dataset) - 1)
print("Standard deviation is", ssd)

#MEAN
def Average(lst):
    return sum(lst) / len(lst)
lst = [10,7,9,11,15,12,13,11,9,10]
average = Average(lst)
 
print("Average of the list =", round(average, 2))

#VARIANCE
def variance(val):
    numb = len(val)
    # m will have the mean value
    m = sum(val) / numb
    # Square deviations
    devi = [(x - m) ** 2 for x in val]
    # Variance
    variance = sum(devi) / numb
    return variance
print("variance is:")
print(variance([6, 6, 3, 9, 4, 3, 6, 9, 7, 8]))
