'''
class living_beings:
    alive=True
    def move(self):
        print("this is able to move")
    def breath(self):
        print("this is also breath")
class animal(living_beings):
    def forest(self):
        print("animal's home is a land")
class fish(living_beings):
    def water(self):
        print("fish's home is water")
a=animal()
print(a.alive)
a.breath()
a.forest()
'''

#multilevel inheritance
'''
class living_beings:
    alive=True
    def move(self):
        print("this is able to move")
    def breath(self):
        print("this is also breath")
class animal(living_beings):
    def land(self):
        print("animal's home is a land")
class wild(animal):
    def __init__(self,name):
        self.name=name
    def forest(self):
        print(self.name," always stay in forest")
t=wild('tiger')
print(t.alive)
t.move()
t.land()
t.forest()
'''

#multiple inheritance
class A:
    def a(self):
        print("this is class a")
class B:
    def b(self):
        print("this is class b")
class C(A,B):
    def c(self):
        print("this is class c")
mi=C()
mi.a()
mi.b()
mi.c()