# Q: You need to take user input and based on those inputs, create the best investment advisor for the user. Take inputs such as name, age, income, etc. And suggest investment options based on tailored inputs. For example: If a person is 75 years old, he should plan more in Debt MF rather than Equity MF. Use best practices

Name = input("Enter Your Name :")
Age  = int(input("Enter Your Age :"))
Income = float(input("Enter Your Annual Income :"))

if Age < 30 and Income < 500000 :
    print(f"Hello {Name}, as you are under 30 and your income is below 500000, we suggest you to invest in Equity Mutual Funds for higher returns.")
    
elif Age <= 30 and  Income >= 500000 and Income < 1000000:
    print(f"Hello {Name}, as you are under 30 and your income is between 500000 and 1000000, we suggest you to invest in a balanced Equity-Debt Mutual Fund ")
    
elif Age <= 30 and Income >= 1000000 :
    print(f"Hello {Name}, as you are between 30 and 60 and your income is below 500000, we suggest you to invest in Debt Mutual Funds for stability.")
    
elif Age >= 30 and Age < 60 and Income >= 500000 and Income < 1000000:
    print(f"Hello {Name}, as you are between 30 and 60 and your income is between 500000 and 1000000, we suggest you to invest in a balanced Equity-Debt Mutual Funds")
    
elif Age >= 30 and Age < 60 and Income >= 1000000:
    print(f"Hello {Name}, as you are between 30 and 60 and your income is above 1000000, we suggest you to invest in Equity Mutual Funds for higher returns.")
    
elif Age >= 60 and Age < 75 and Income < 500000:
    print(f"Hello {Name}, as you are between 60 and 75 and your income is below 500000, we suggest you to invest in Debt Mutual Funds for stability. ")
    
elif Age >= 60 and Age < 75 and Income < 1000000:
    print(f"Hello {Name}, as you are between 60 and 75 and your income is between 500000 and 1000000, we suggest you to invest in a balanced Equity-Debt Mutual Funds")
    
elif Age >= 60 and Age < 75 and Income < 1000000:
    print(f"Hello {Name}, as you are between 60 and 75 and your income is above 1000000, we suggest you to invest in Equity Mutual Funds .")
    
        
   