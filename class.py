# class Example:
#     number=0
#     name=''
#     age=18
#     def __init__(self,number,name):
#         self.number=number
#         self.name=name
#     def countage(self,age):
#         self.age=age
# ex=Example(1,'kaif')
# print(ex.number)
# print(ex.name)
# print(ex.age)
# ex.countage(19)
# print("after 1 year :: ",ex.age)
import math
class Area:
    length=0
    width=0
    def area(self,length,width):
        self.length=length
        self.width=width
        return self.length*self.width
area_of_squere=Area()
print(area_of_squere.area(5,4))