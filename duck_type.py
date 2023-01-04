class duck1:
    def walk(self):
        print("duck1 is walking")
    def talk(self):
        print("duck1 is talking")
class duck2:
    def walk(self):
        print("duck2 is walking")
    def talk(self):
        print("duck2 is talking")
class person():
    def catch(self,class_name):
        class_name.walk()
        class_name.talk()
        print(class_name," is catch")
duck1=duck1()
duck2=duck2()
person=person()
person.catch(duck1)
print()
person.catch(duck2)