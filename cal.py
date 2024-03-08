def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Error! Cannot divide by zero!"
        result /= num
    return result

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

while True:
    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator...")
        break

    if choice in ('1', '2', '3', '4'):
        nums = input("Enter numbers separated by space: ").split()
        nums = [float(num) for num in nums]

        if choice == '1':
            print("Result:", add(nums))
        elif choice == '2':
            print("Result:", subtract(nums))
        elif choice == '3':
            print("Result:", multiply(nums))
        elif choice == '4':
            print("Result:", divide(nums))
    else:
        print("Invalid Input")
