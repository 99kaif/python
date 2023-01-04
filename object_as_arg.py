class car:
    color=None
def change_color(class_name,color):
    class_name.color=color
car_1=car()
car_2=car()
car_3=car()
change_color(car_1,'black')
change_color(car_2,'blue')
change_color(car_3,'red')
print(car_1.color)
print(car_2.color)
print(car_3.color)
