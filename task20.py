// Mean 

def find_mean(numbers):

    
    sum = 0
    count = 0
    for num in numbers:
        sum += num
        count += 1
    mean = sum / count
    return mean


numbers = [10,7,9,11,15,12,13,11,9,10]
mean = find_mean(numbers)
print("Mean:", mean)



// Standard Deviation

import math

def calculate_standard_deviation(numbers):
    # calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)

    # calculate the sum of the squares of the differences between each number and the mean
    squared_diff_sum = sum([(number - mean) ** 2 for number in numbers])

    # divide the sum of the squares by the number of numbers, and take the square root
    std_dev = math.sqrt(squared_diff_sum / len(numbers))

    return std_dev
numbers = [10,7,9,11,15,12,13,11,9,10]
std_dev = calculate_standard_deviation(numbers)
print(std_dev)

// Variance

def calculate_variance(numbers):
    # calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)

    # calculate the sum of the squares of the differences between each number and the mean
    squared_diff_sum = sum([(number - mean) ** 2 for number in numbers])

    # divide the sum of the squares by the number of numbers
    variance = squared_diff_sum / len(numbers)

    return variance
numbers = [10,7,9,11,15,12,13,11,9,10]
variance = calculate_variance(numbers)
print(variance)
