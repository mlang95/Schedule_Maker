import random
from random import shuffle
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
        self.Max_Days = 6
        self.Working_Days = 0
        self.hire_date = hired
        self.employee_type = employee_type
class Store:
    def __init__(self,Employees):
        self.Department_Names = ["Night","Merch","Cash","Opt","Tech","Maint","Bake","Food","Major"]
        self.Department_List = []
        self.Minimum_Capacity = 0
        self.Maximum_Capacity = 0
        #Generate all the departments by name and their capacities
        for Department_Name in Department_Names:
            Min = random.randint(3,6)
            Department_List.append(Department(Department_Name,Min,Min+random.randint(3,25),Employees))
    def Get_Min(self):

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

    def Make_Schedule(self):
        Days = ['M','T','W','R','F','Sat','Sun']      
        for Emp in range(len(self.Employees)):
            for Day in range(len(Days)):
                for Depart in range(len(self.Employees[Emp].departments)):
                    if self.Department_Name == self.Employees[Emp].departments[Depart]:
                        if self.Employees[Emp].availability[Day] == 'Y' and self.Employees[Emp].working[Day] == 0:
                            if self.Capacity[Day] < self.Max_Capacity[Day]:
                                if self.Employees[Emp].Working_Days < self.Employees[Emp].Max_Days:
                                    if self.Employees[Emp].Schedule[Day] == 'Off ':
                                        self.Employees[Emp].working[Day] = 1
                                        self.Capacity[Day] += 1
                                        self.Employees[Emp].Schedule[Day] = self.Department_Name
                                        self.Employees[Emp].Working_Days+=1
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
        for x in range(len(List_of_Employees)):
            print(List_of_Employees[x].name, end='  |')
            for i in range(len(Days)):
                print(List_of_Employees[x].Schedule[i], end = '\t')
            print()
List_of_First_Names = ['Mary','Sue','Jerry','Harry','Joe','Matt','Meredith',"Catherine",'Chris',"Stayfahn","Ken",'Catherine','George','Allison','Taylor','Wesley','Jordan','Jim','Craig','Michael','Richard','Timothy','Tim']
List_of_Last_Names = ['Smith','Kennedy','Williams','Space','Wiggins','Price','Lang','Lee','Coles','Buffet','Clark','Banks','Johnson','Jacobs','Laurence','Adams','Reeder','Carpenter','Taylor','Button','Harden','Trader','Wilson','Washington','Wesley','Barcley','Jordan','Lincoln','Bush','Doyle','Armesto','Brooks','Bailey','Sinegal','Jelinek','Michaels','Richards']
List_of_Departments = ['Merch','Cash','Assist','Night','Maint','Food']
List_of_Employees = []
for i in range(50): #generate employees and their conditions
    Y_N = ['Y','N','Y',"Y","Y","Y","N"]
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
    print(List_of_Employees[i].name,List_of_Employees[i].hire_date,List_of_Employees[i].departments)
Night_Merch = Department("Night",4,5,List_of_Employees)
Night_Merch.Make_Schedule()
Morning_Stocker = Department("Merch",10,15,List_of_Employees)
Morning_Stocker.Make_Schedule()
Front_End = Department("Cash",15,20,List_of_Employees)
Front_End.Make_Schedule()
Majors = Department("Major",3,5,List_of_Employees)
Majors.Make_Schedule()
Bakery = Department("Bake",4,7,List_of_Employees)
Bakery.Make_Schedule()
Maintenance = Department("Maint",6,10,List_of_Employees)
Maintenance.Make_Schedule()
Technicians = Department("Tech",3,6,List_of_Employees)
Technicians.Make_Schedule()

Optical = Department("Opt",2,3,List_of_Employees)
Optical.Make_Schedule()
Optical.Print_Schedule()