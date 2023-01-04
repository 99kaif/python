class A:
    def a(self):
        print("this is class a")
class B(A):
    def b(self):
        print("this is class b")
    def a(self):
        print("this is override class a")
oc=B()
oc.a()
oc.b()