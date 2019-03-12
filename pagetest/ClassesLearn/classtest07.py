
class Parent01(object):
    def __init__(self,name):
        self.name = name
        print(Parent01.__name__)

    def parent01Method(self):
        print("这是parent01Method")

class Parent02(object):
    def __init__(self,name):
        self.name = name
        print(Parent02.__name__)

    def parent02Method(self):
        print("这是parent02Method")

class Child(Parent01,Parent02):
    def __init__(self,name):
        self.name = name
        print(Child.__name__)

    def childMethod(self):
        print("这是childMethod")

c = Child('CC')
c.parent01Method()
c.parent02Method()
c.childMethod()

if issubclass(Child,Parent01):      # 判断一个类是另外一个类的子类或子孙类，则返回True;反之，返回False
    print("类%s 是 类%s 的子类"%(Child.__name__,Parent01.__name__))

if isinstance(c,Child):     # 判断一个对象是一个类的实例对象或者其子类的实例对象，则返回Ture；反之，返回False
    print("对象%s 是 类%s 的实例对象" %(c,Child.__name__))










