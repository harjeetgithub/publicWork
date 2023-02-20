numbers = [10, 7, 9, 11, 15, 12, 13, 11, 9, 10]
print("Enter 1 to calculate mean.")
print("Enter 2 to calculate standard deviation.")
print("Enter 3 to calculate variance.")
choice = int(input("Enter your choice: "))

if choice == 1:
    sum = 0
    count = 0
    while count < len(numbers):
        sum += numbers[count]
        count += 1
    mean = sum / len(numbers)
    print("The mean is:", mean)

elif choice == 2:
    sum = 0
    count = 1
    while count < len(numbers):
        sum += (numbers[count-1] - sum/count)**2
        count += 1
    variance = sum / len(numbers)
    std_dev = variance ** 0.5
    print("The standard deviation is:", std_dev)

elif choice == 3:
    sum = 0
    count = 1
    while count < len(numbers):
        sum += (numbers[count-1] - sum/count)**2
        count += 1
    variance = sum / len(numbers)
    print("The variance is:", variance)

else:
    print("Invalid input. Please enter a number between 1 and 3.")

