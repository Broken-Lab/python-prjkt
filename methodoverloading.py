class Person:
    def Hello(self,name=None):
        if name is not None:
            print("Hello" + name)
        else:
            print("Hello")
#Create Instance
obj = Person()
obj.Hello()
obj.Hello("Sourav")