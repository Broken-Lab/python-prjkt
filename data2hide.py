class MyClass:
    __hiddenVariable = 0

    def add(self,increment):
        self.__hiddenVariable += increment
        print(self.__hiddenVariable)

myObject = MyClass()
myObject.add(2)
myObject.add(5)

#this line will cause error if we try to access hidden variable with class object
# print(myObject.__hiddenVariable)
print(myObject._MyClass__hiddenVariable)