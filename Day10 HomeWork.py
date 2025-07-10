#Q1: Write a program that prints the multiplication table for any number.
a = int(input("Enter The Number:"))
print(f"Multiplication Table for {a}:")
for i in range(1, 11):
    print(f"{a} * {i} = {a * i}")
    
#Q2: Calculate Sum of numbers in the list [1,4,6,4,9]
lst_num = [10, 41, 30, 59, 12, 16, 32]
sum_of_num = sum(lst_num)
print(f"Sum of numbers in the list {lst_num} is: {sum_of_num}")
