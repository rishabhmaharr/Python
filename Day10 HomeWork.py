#Q1: Write a program that prints the multiplication table for any number.
a = int(input("Enter The Number:"))
print(f"Multiplication Table for {a}:")
for i in range(1, 11):
    print(f"{a} * {i} = {a * i}")
    
#Q2: Calculate Sum of numbers in the list [1,4,6,4,9] 
numbers = [1, 4, 6, 4, 9]
total_sum = 0

for number in numbers:
    if number > 0:  # Check if the number is positive
        total_sum += number
    else:
        print(f"Bypassing negative number: {number}")

print("The sum of the numbers is:", total_sum)

