# -*- coding: UTF-8 -*-


class Employee:
    '所有员工的基类'
    empCount = 0    # 类变量，其值将在这个类的所有实例之间共享

    # 构造函数，创建实例后会调用该方法
    def __init__(self,name,salary): # self代表类的实例，在定义类方法时必须有，虽然调用时不需要传入参数
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" %Employee.empCount)

    def displayEmployee(self):
        print("Name :" + str(self.name) + ", Salary: " + str(self.salary))

#"创建 Employee 类的第一个对象"
emp1 = Employee("Zara",2000)
#"创建 Employee 类的第二个对象"
emp2 = Employee("Manni",5000)

# print("Total Emplotee %d" %Employee.empCount)
#
# emp1.displayEmployee()
# emp2.displayEmployee()
#
# emp1.displayCount()
# emp2.displayCount()

# emp1.age = 7
# emp1.age = 8
# del emp1.age
# print(emp1.age)
#
# setattr(emp1,'age',8)
# if hasattr(emp1,'age'):
#     print('yes')
# else:
#     print('no')
# print(emp1.age)
# delattr(emp1,'age')
# print(getattr(emp1,'age'))

# print(Employee.__dict__)
# print(Employee.__doc__)
# print(Employee.__name__)
# print(Employee.__module__)
print(Employee.__bases__)