# Q1. Student Report System (Class, Object, Encapsulation)
# Create a class Student with:
# Private attributes: __name, __marks
# A method set_details(name, marks)
# A method get_result() to print pass/fail (pass if marks >= 40)
 
# Sample Output:
# Name: Ram
# Marks: 85
# Result: Pass
class Student:
    def __init__(self):
        self.__name = ""
        self.__marks = 0

    def set_details(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_result(self):
        print(f"Name: {self.__name}")
        print(f"Marks: {self.__marks}")
        if self.__marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


# Creating object and using the class
s1 = Student()
s1.set_details("Ram", 85)
s1.get_result()

# Q2. Animal Kingdom (Inheritance + Polymorphism)
# Create a base class Animal with method speak()
# Then create 2 subclasses:
# Dog → speak() should print "Barks"
# Cat → speak() should print "Meows"
# Loop through list of objects and call speak() to show polymorphism.
 # Sample Output:
# Barks
# Meows
# Base class

class Animal:
    def speak(self):
        print("Animal speaks")

# Subclass Dog
class Dog(Animal):
    def speak(self):
        print("Barks")

# Subclass Cat
class Cat(Animal):
    def speak(self):
        print("Meows")


# List of animal objects demonstrating polymorphism
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
    
#     Q3. Payment Gateway (Abstraction + Inheritance + Method Overriding)
# Use abc module.
# Create abstract class Payment with abstract method make_payment().
# Create subclasses:
# CreditCard → prints "Paid using credit card"
# UPI → prints "Paid using UPI"
 # Sample Output:
# Paid using credit card
# Paid using UPI

from abc import ABC, abstractmethod

# Abstract base class
class Payment(ABC):
    @abstractmethod
    def make_payment(self):
        pass

# Subclass: CreditCard
class CreditCard(Payment):
    def make_payment(self):
        print("Paid using credit card")

# Subclass: UPI
class UPI(Payment):
    def make_payment(self):
        print("Paid using UPI")


# Creating objects and calling make_payment()
p1 = CreditCard()
p2 = UPI()

p1.make_payment()
p2.make_payment()

