numb = [10,7,9,11,15,12,13,11,9,10]
no = len(numb)
summ = sum(numb)
mean = summ / no
print("The mean or average of all these numbers (", numb, ") is", str(mean))
#VARIANCE
def variance(val):
    numb = len(val)
    # m will have the mean value
    m = sum(val) / numb
    # Square deviations
    devi = [(x - m) ** 2 for x in val]
    # Variance
    variance = sum(devi) / numb
