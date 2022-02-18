class personal: #Create Class Named Personal
    def persinfo(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

class academic: #Create Class Named Academic
    def acainfo(self,qua,percentage):
        self.qua = qua
        self.percentage = percentage

class biodata(personal,academic): # Inherit above classes with biodata class
    def __init__(self,name,gender,age,qua,percentage):
        self.persinfo(name,gender,age)
        self.acainfo(qua,percentage)
        
inp1 = input("Enter Your Name : ") #Take input from user
inp2 = input("Enter Your Gender : ")
inp3 = input("Enter Your Age : ")
inp4 = input("Enter Your Qualification : ")
inp5 = input("Enter Your Percentage : ")
print ("--------------------------")

per = biodata(inp1,inp2,inp3,inp4,inp5) # Create Object And Pass Variables

print ("Name : ",per.name) # Display Output
print ("Gender : ",per.gender)
print ("Age : " , per.age)
print ("Qualification : " , per.qua)
print ("Percentage :" , per.percentage)

