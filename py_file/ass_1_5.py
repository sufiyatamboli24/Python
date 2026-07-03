"""write a class Person which accept name and age from user and print them using function """
class person:
    def get(self):
        self.name=input("Enter the name:")
        self.age=input("Enter the age:")
    def put(self):
        print("Name:",self.name)    
        print("age:",self.age)

p=person()
p.get()
p.put()       
















      
