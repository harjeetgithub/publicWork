import math

def calculate_statistics(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    variance = sum((x - mean) ** 2 for x in numbers) / n
    std_dev = math.sqrt(variance)

    sorted_numbers = sorted(numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n//2-1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]

    return mean, median, std_dev, variance

# Example usage
numbers = [1,10,7,10,8,9,15,6,9]
mean, median, std_dev, variance = calculate_statistics(numbers)
print("Mean:", mean)
print("Median:", median)
print("Standard deviation:", std_dev)
print("Variance:", variance)
