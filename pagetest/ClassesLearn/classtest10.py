

class JustConter(object):

    def __secretCount(self,count):
        print("secretCount: %d"%count)

    def publictCount(self,count):
        print("publicCount: %d" %count)


c = JustConter()
c.publictCount(2)
c.__secretCount(1)



