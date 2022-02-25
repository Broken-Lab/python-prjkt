class MyClass:
    __hiddenVar = 0 
    def add(self,increment):
        self.__hiddenVar += increment
        print(self.__hiddenVar)
myObject = MyClass()
myObject.add(3)
myObject.add(8)

#print(myObject.__hiddenVar) #we cant access with this method 
print(myObject._MyClass__hiddenVar)