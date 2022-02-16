class Employee():
    def main(self,name,idno,position,salary):
        self.name=name
        self.idno=idno
        self.position=position
        self.salary = salary

    def input(self):
        n=int(input("Enter the number of employees:"))
        for i in range(n):
            self.name=input("Name:")
            self.idno=input("Idno:")
            self.position=input("position:")
            self.salary=input("salary:")

            print("Name:", self.name, "Idno:", self.idno, "position:", self.position,
                  "salary:", self.salary)

if __name__=='__main__':
        result=Employee()
        result.input()
        
# employee class code in Python
# class definition
class Employee:
    __id=0
    __name=""
    __gender=""
    __city=""
    __salary=0
	
	# function to set data 
    def setData(self,id,name,gender,city,salary):
        self.__id=id
        self.__name = name
        self.__gender = gender
        self.__city = city
        self.__salary = salary
	
	# function to get/print data
    def showData(self):
        print("Id\t\t:",self.__id)
        print("Name\t:", self.__name)
        print("Gender\t:", self.__gender)
        print("City\t:", self.__city)
        print("Salary\t:", self.__salary)

# main function definition
def main():
    #Employee Object
    emp=Employee()
    emp.setData(1,'pankaj','male','delhi',55000)
    emp.showData()
	
if __name__=="__main__":
    main()