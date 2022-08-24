from function import addNumber, multiplyNumber, divideNumber

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
#  Calling out user-defined function 
sum = addNumber(num1, num2)
print("Sum of two numbers is: ", sum) 

multiply = multiplyNumber(num1, num2)
print("multiply of two numbers is: ", multiply) 

divide = divideNumber(num1, num2)
print("multiply of two numbers is: ", divide) 