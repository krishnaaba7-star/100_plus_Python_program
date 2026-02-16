# Find the largest among three numbers
# solution 1 : using conditional statements
num1 = 102
num2 = 56
num3 = 78
if (num1>num2) and (num1>num3):
    print(num1 , "is the largest number")
elif (num2>num1) and (num2>num3):
    print(num2 , "is the largets number")
else:
    print(num3 , "is the largest number")


#solution 2 : with userinput

number1 = int(input("Enter Num 1:"))
number2 = int(input("Enter Num 2:"))
number3 = int(input("Enter Num 3:"))
if (number1>number2) and (number1>number3):
    print(number1 , "is the largest number")
elif (number2>number1) and (number2>number3):
    print(number2 , "is the largets number")
else:
    print(number3 , "is the largest number")
