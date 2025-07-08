# HomeWork Day7
# #Q1:CREATE TWO LISTS OF MULTIPLE DATATYPES AND PRACTICE THE FOLLOWING FUNCTIONS ON THEM--> append, insert, extend, remove, delete & sort (DESCENDING)
list1 = [1, 8, 19, "Apple", "Watermelon"]
list2 = [18, 12, 23, "Banana", "Grapes"]

# Append
list1.append("Mango")
print(f"{list1}")

list2.append(95)
print(f"{list2}")

# Insert
list1.insert(2, "Orange")
print(f"{list1}")

list2.insert(1, 45)
print(f"{list2}")

# Extend
list1.extend(list2)
print(f"{list1}")

# Remove
list1.remove("Apple")
print(f"{list1}")

list2.remove(23)
print(f"{list2}")


#Q2: Write a program to count how many times the number 3 appears in a list.
num = [1, 2, 3, 5, 3, 9, 6, 3, 4, 3]
count_of_3 = num.count(3)
print(f"The number 3 appears {count_of_3} times in the list.")

#Q3: Create a list of 5 fruits and print the second and last fruit.
fruits = ["Apple", "Banana", "Cheery", "Mango", "WaterMelon"]
print(f"The Second fruit is: {fruits[1]}")
print(f"The Last Fruit is: {fruits[-1]}") 






