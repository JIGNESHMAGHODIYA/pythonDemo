class PrintDemo:

    def __init__(self, prt):
        self.strs = prt

    def show(self):
        print(self.strs)

    def update(self,i):
        self.strs += ' ' + str(i)



class main:
    objs = []
    //names = ['jay','sachin','yash','paresh','dilip','vimal','mukesh','mahesh','vijay','ravi']
    name=['sachin','jignesh']

    for i in names:
        objs.append(PrintDemo(i))

    for num,i in enumerate(objs) :
        objs[num].show()
        objs[num].update(num)
        objs[num].show()
        print()


