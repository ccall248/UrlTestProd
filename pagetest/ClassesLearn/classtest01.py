class Test:
    '这是类的帮助信息'
    def prt(self):
        print(self)
        print(self.__class__)
        print(self.__doc__)

t = Test()
t.prt()