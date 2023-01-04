class Car:
    def drive(self):
        print("drive")
        return self
    def brek(self):
        print("break")
        return self
    def stop(self):
        print("stop")
        return self
car=Car()
car.drive().brek().stop()

print()
print()

car.drive()\
    .brek()\
    .stop()