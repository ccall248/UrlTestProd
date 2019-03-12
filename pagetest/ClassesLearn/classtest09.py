
class JustConter(object):
    __secretCount = 0   # 私有变量
    publicCount = 0     # 公有变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

c = JustConter()
c.count()
c.count()
print(c.publicCount)
print(c._JustConter__secretCount)
print(c.__secretCount)














