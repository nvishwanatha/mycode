# Python3 program to
# demonstrate instantiating
# a class


class Dog:
    # A simple class
    # attribute
    attr1 = "Animal"
    attr2 = "dog"

    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)


# Driver code
# Object instantiation
Mammal = Dog()

# Accessing class attributes
# and method through objects
print(Mammal.attr1)
Mammal.fun()
