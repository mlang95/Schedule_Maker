import random
from random import shuffle
import numpy as np
class Shift:
    def __init___ (self,name,size,length,Employees):
        self.name = name
        self.shift_size = size
        self.shift_type = Employees.employee_type
        self.shift_length = Get_Length(Employees)
        self.shift_start = start
        self.shift_end = end
    def Get_Length(self,Employees):
        if self.Employees.employee_type == 'full-time':
            return 8
        elif self.Employees.employee_type == 'part-time':
            return 5
        elif self.Employees.employee_type == 'seasonal':
            return 5
class Employee:
    def __init__ (self, name, departments, availability,hired,employee_type):
        self.name =name
        self.departments = departments
        self.availability = availability
        self.working = [0 for x in range(7)]
        self.Schedule = ['Off ' for x in range(7)]
        self.Max_Days = 5
        self.Working_Days = 0
        self.hire_date = hired
        self.employee_type = employee_type
class Store:
    def __init__(self,Departments,Employees):
        self.Department_Names = [department.Department_Name for department in Departments]
        self.Department_List = Departments
        self.Shift_Min_Capacity = 0
        self.Shift_Max_Capacity = 0
        self.Shift_Capacity = 0
        self.Dep_Min_Capacity = 0
        self.Dep_Max_Capacity = 0
        self.Dep_Capacity = 0

        self.Employees = Employees
        self.trainingDict = {dep:0 for dep in self.Department_Names}
        #Generate all the departments by name and their capacities
        self.Get_Capacities()
        self.Get_Department_Capacity()
        self.Get_Understaffed_Departments()
        self.Get_Department_Training()
        '''
        for Department_Name in Department_Names:
            Min = random.randint(3,6)
            Department_List.append(Department(Department_Name,Min,Min+random.randint(3,25),Employees))
        '''
    def Get_Capacities(self):
        Days = ['M','T','W','R','F','Sat','Sun']
        for emp in self.Employees:
            for day in range(len(Days)):
                if emp.availability[day] == "Y":
                    self.Shift_Max_Capacity += 1
                    if emp.working[day]:
                        self.Shift_Capacity +=1
        for dep in self.Department_List:
            for day in range(len(Days)):
                self.Dep_Capacity += dep.Capacity[day]
                self.Dep_Max_Capacity += dep.Max_Capacity[day]
                self.Dep_Min_Capacity += dep.Min_Capacity
                self.Shift_Min_Capacity = self.Dep_Min_Capacity
        return self

    def Get_Department_Capacity(self):
        print("Department Capacity")
        #[[print("%s: %s" % (dep.Department_Name,day))  for day in dep.Capacity ] for dep in self.Department_List]
        Days = ['M','T','W','R','F','Sat','Sun']
        
        print("\tM\tT\tW\tR\tF\tSat\tSun")
        print("------------------------------------------------------------------------------")
        sortedList = sorted(self.Department_List, key=lambda y: y.Department_Name, reverse=True)
        for x in range(len(sortedList)):
            name =self.Department_List[x].Department_Name
            print( name + " "*(len(max([x.Department_Name for x in sortedList]))-len(name)), end='  |')
            for i in range(len(Days)):
                print("%s/%s" % (self.Department_List[x].Capacity[i],self.Department_List[x].Min_Capacity), end = '\t')
            print()

    def Get_Department_Training(self):
        print("Trained Employees")
        print("------------------------------------------------------------------------------")
        for dep in self.Department_List:
            for emp in self.Employees:
                if dep.Department_Name in emp.departments:
                    self.trainingDict[dep.Department_Name] += 1
        [print("%s: %s" % (key,self.trainingDict[key])) for key in self.trainingDict]

    def Get_Understaffed_Departments(self):
        print("Understaffed Departments")
        Days = ['M','T','W','R','F','Sat','Sun']
        print("\tM\tT\tW\tR\tF\tSat\tSun")
        print("------------------------------------------------------------------------------")
        sortedList = sorted(self.Department_List, key=lambda y: y.Department_Name, reverse=True)
        for x in range(len(sortedList)):
            name =self.Department_List[x].Department_Name
            print( name + " "*(len(max([x.Department_Name for x in sortedList]))-len(name)), end='  |')
            for i in range(len(Days)):
                if self.Department_List[x].Capacity[i] < self.Department_List[x].Min_Capacity:
                    print("%s/%s" % (self.Department_List[x].Capacity[i],self.Department_List[x].Min_Capacity), end = '\t')
                else:
                    print("--",end = "\t")
            print()


class Department:
    def __init__(self, name, min_capacity, max_capacity,Employees):
        self.Department_Name = name
        self.Min_Capacity = min_capacity
        self.Max_Capacity = [max_capacity for x in range(7)]
        self.Employees = Employees
        self.Capacity = [0 for x in range(7)]

    def Normalise_Name_Length(self):
        Max_Length = 0
        for x in range(len(self.Employees)):
            
            if len(self.Employees[x].name) > Max_Length:
                Max_Length = len(self.Employees[x].name)
        for x in range(len(self.Employees)):
            while len(self.Employees[x].name) < Max_Length:
                self.Employees[x].name += ' '
        return Max_Length

    def Fill_Schedule(self):
        Days = ['M','T','W','R','F','Sat','Sun']      
        for Emp in range(len(self.Employees)):
            for Day in range(len(Days)):
                if self.Department_Name in self.Employees[Emp].departments:
                    if self.Employees[Emp].availability[Day] == 'Y' and self.Employees[Emp].working[Day] == 0:
                        if self.Capacity[Day] < self.Max_Capacity[Day]:
                            if self.Employees[Emp].Working_Days < self.Employees[Emp].Max_Days:
                                if self.Employees[Emp].Schedule[Day] == 'Off ':
                                    self.Employees[Emp].working[Day] = 1
                                    self.Capacity[Day] += 1
                                    self.Employees[Emp].Schedule[Day] = self.Department_Name
                                    self.Employees[Emp].Working_Days+=1

        return self

    def Min_Schedule(self):
        Days = ['M','T','W','R','F','Sat','Sun']      
        for Emp in range(len(self.Employees)):
            for Day in range(len(Days)):
                if self.Department_Name in self.Employees[Emp].departments:
                    if self.Employees[Emp].availability[Day] == 'Y' and self.Employees[Emp].working[Day] == 0:
                        if self.Capacity[Day] < self.Min_Capacity:
                            if self.Employees[Emp].Working_Days < self.Employees[Emp].Max_Days:
                                if self.Employees[Emp].Schedule[Day] == 'Off ':
                                    self.Employees[Emp].working[Day] = 1
                                    self.Capacity[Day] += 1
                                    self.Employees[Emp].Schedule[Day] = self.Department_Name
                                    self.Employees[Emp].Working_Days+=1

        return self
                                    #print("%s is working on %s for the %s self.Employees[x].Schedule" % (self.Employees[x].name, Days[i],Employees[x].Schedule[i]))
                #self.Schedule.append([self.Employees[x].name,Days[i],self.Employees[x].Schedule[i]])
    def Print_Schedule(self):
        Max_Length = self.Normalise_Name_Length()
        x = ' '
        Spacing = ''
        while len(Spacing) < (Max_Length-4):
            Spacing += x
        Days = ['M','T','W','R','F','Sat','Sun']
        
        print("Name" + Spacing +"\tM\tT\tW\tR\tF\tSat\tSun")
        print("------------------------------------------------------------------------------")
        sortedList = sorted(List_of_Employees, key=lambda y: y.Working_Days, reverse=True)
        for x in range(len(sortedList)):
            print(List_of_Employees[x].name, end='  |')
            for i in range(len(Days)):
                print(List_of_Employees[x].Schedule[i], end = '\t')
            print()
List_of_First_Names = ['Mary','Sue','Jerry','Harry','Joe','Matt','Meredith',"Catherine",'Chris',"Stayfahn","Ken",'Catherine','George','Allison','Taylor','Wesley','Jordan','Jim','Craig','Michael','Richard','Timothy','Tim']
List_of_Last_Names = ['Smith','Kennedy','Williams','Space','Wiggins','Price','Lang','Lee','Coles','Buffet','Clark','Banks','Johnson','Jacobs','Laurence','Adams','Reeder','Carpenter','Taylor','Button','Harden','Trader','Wilson','Washington','Wesley','Barcley','Jordan','Lincoln','Bush','Doyle','Armesto','Brooks','Bailey','Sinegal','Jelinek','Michaels','Richards']
List_of_Departments = ['Merch','Cash','Assist','Night','Maint','Food',"Bake","Tech","Opt","Major"]
List_of_Employees = []
for i in range(100): #generate employees and their conditions
    availability = random.randint(2,5)
    Y_N = ["Y" for x in range(availability)] + ["N" for x in range(7-availability)]
    random.shuffle(Y_N)
    Availability = Y_N
    Trained_Departments = random.randint(2,4)
    Trained = []
    for x in range(Trained_Departments):
        Test = random.choice(List_of_Departments)
        if Test in Trained:
            pass
        else:
            Trained.append(Test)
        Name = random.choice(List_of_First_Names) + ' ' + random.choice(List_of_Last_Names)
        hired = random.randint(2000,2017)
        employee_type_list = ['seasonal','part-time','full-time']
        employee_type = random.choice(employee_type_list)
    List_of_Employees.append(Employee(Name,Trained,Availability,hired,employee_type))
List_of_Employees = sorted(List_of_Employees,key=lambda x: (x.employee_type,x.hire_date),reverse=False)
for i in range(len(List_of_Employees)):
    pass
    #print(List_of_Employees[i].name,List_of_Employees[i].hire_date,List_of_Employees[i].departments)
Maintenance = Department("Maint",6,10,List_of_Employees)
Maintenance.Min_Schedule()
Technicians = Department("Tech",3,6,List_of_Employees)
Technicians.Min_Schedule()
Optical = Department("Opt",2,3,List_of_Employees)
Optical.Min_Schedule()
Front_End = Department("Cash",15,20,List_of_Employees)
Front_End.Min_Schedule()
Night_Merch = Department("Night",4,5,List_of_Employees)
Night_Merch.Min_Schedule()
Morning_Stocker = Department("Merch",10,15,List_of_Employees)
Morning_Stocker.Min_Schedule()
Majors = Department("Major",3,5,List_of_Employees)
Majors.Min_Schedule()
Bakery = Department("Bake",4,7,List_of_Employees)
Bakery.Min_Schedule()
Bakery = Department("Food",3,6,List_of_Employees)
Bakery.Min_Schedule()
Night_Merch.Fill_Schedule()
Morning_Stocker.Fill_Schedule()
Front_End.Fill_Schedule()
Majors.Fill_Schedule()
Bakery.Fill_Schedule()
Bakery.Fill_Schedule()
Maintenance.Fill_Schedule()
Technicians.Fill_Schedule()
Optical.Fill_Schedule()

Optical.Print_Schedule()
Store1 = Store([Night_Merch,Morning_Stocker,Front_End,Majors,Bakery,Maintenance,Technicians,Optical],List_of_Employees)
print("Shifts Scheduled: {cap}\nShifts Available: {max}".format(cap=Store1.Shift_Capacity,max=Store1.Shift_Max_Capacity))
print("Department Scheduled: {cap}\nDepartment Minimum: {max}".format(cap=Store1.Dep_Capacity,max=Store1.Dep_Min_Capacity))
