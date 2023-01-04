class rectengle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
class squere(rectengle):
    def __init__(self, length, width):
        super().__init__(length, width)
    def sq(self):
        print(self.length*self.width)
class cube(rectengle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height=height
    def cb(self):
        print(self.length*self.width*self.height)
a=squere(4,5)
b=cube(3,5,6)
a.sq()
b.cb()