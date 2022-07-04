# Python3 program to get input from user

# accepting integer from the user
# the return type of input() function is string ,
# so we need to convert the input to integer
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

num3 = num1 * num2
print("Product is: ", num3)

# Python program to illustrate
# selection statement

num1 = 34
if (num1 > 12):
    print("Num1 is good")
elif (num1 > 35):
    print("Num2 is not gooooo....")
else:
    print("Num2 is great")