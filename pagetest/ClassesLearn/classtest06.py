
class Parent(object):
    parentAttr = 100

    def __init__(self):
        print("调用父类构造方法")

    def parentMethod(self):
        print("调用父类方法")

    def setAttr(self,attr):
       Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性 :" + str(Parent.parentAttr))

class Child(Parent):
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print("调用子类方法")

c = Child()         # 子类构造方法重写了，所以直接调用子类构造方法
c.childMethod()     # 调用子类方法
c.parentMethod()    # 子类调用父类的方法
c.setAttr(200)      # 子类调用父类的方法，设置属性并赋值
c.getAttr()         # 子类调用父类方法，获取属性值









