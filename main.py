import myfunc #import calculator functions from myfunc
num1 = int(input("Enter First Number: ")) #take input from user
num2 = int(input("Enter Second Number: "))
print(f"The Addition of {num1} and {num2} is",myfunc.add(num1,num2))
print(f"The Substraction of {num1} and {num2} Is",myfunc.sub(num1,num2))
print(f"The Multiplication of {num1} and {num2} Is",myfunc.mul(num1,num2))
print(f"The Division of {num1} and {num2} Is",myfunc.div(num1,num2))
