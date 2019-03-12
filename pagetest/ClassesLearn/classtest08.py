
class Parent:
    def myMethod(self):
        print("调用父类的方法")

class Child(Parent):
    def myMethod(self):
        print("调用子类的方法")

c = Child()     # 实例化子类
c.myMethod()    # 子类调用重写的方法








