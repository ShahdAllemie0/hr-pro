
class Employee:
   #Employee class here



   def __init__(self, name, age,salary,employment_year):
       self.name=name
       self.age=age
       self.salary=salary
       self.employment_year=employment_year

   def get_working_years(self):
       from datetime import date
       today = date.today().year
       working_years=today-self.employment_year
       return  working_years


   def __str__(self):
       
       return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years:{self.get_working_years()}' 
      



class Manager(Employee):
    #Manager class here
    def __init__(self, name, age,salary,employment_year,bonus_percentage):
        Employee.__init__(self, name, age,salary,employment_year)
        self.bonus_percentage=bonus_percentage

    def get_bonus(self):
        return self.bonus_percentage * self.salary

    def __str__(self):
      return super().__str__()+f', Bonus: {self.get_bonus()}'    




def main():
    # main code here
  employee=[]
  manager=[]
  listt=["1. Show Employees","2. Show Managers","3. Add An Employee","4. Add A Manager","5. Exit"]

  print("Welcome to HR Pro 2020")
  for x in listt:
       print(x)
  op=int(input("What would you like to do?") )    
  
  while op!=5:
    if op==1:
      for x in employee:
        print(x)
    elif op==2:
      for x in employee:
        print(x)
    elif op==3:
      name=input("Name:")
      age=int(input("Age:"))
      salary=int(input("Salary:"))
      em_year=int(input("Employement year:"))
      e=Employee(name,age,salary,em_year)
      employee.append(e)
      print("Employee added succesfully")
    elif op==4:
      name=input("Name:")
      age=input("Age:")
      salary=input("Salary:")
      em_year=input("Employement year:")
      bonus=input("Bonus Percentage:")
      m=Manager(name,age,salary,em_year,bonus)
      manager.append(m)
      print("Manager added succesfully")
    else:
      break  


      


    for x in listt:
      print(x)
    op=int(input("What would you like to do?") )   
    

if __name__ == '__main__':
    main()
