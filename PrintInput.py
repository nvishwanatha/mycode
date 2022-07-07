x, y = input(), input()
print("x=",x,"y=",y)

x, y = input().split()
print("x=",x,"y=",y)

# Read two numbers from input and typecasts them to int using
# list comprehension
x, y = [int(x) for x in input().split()]

print (x,y)


