#abstractmethod is a use for only decoration not implemantion
from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
class car(vehicle):
    def go(self):
        print("this car is already in motion")
class motorcycle(vehicle):
    def go(self):
        print("this motorcycle is already in motion")
car=car()
motorcycle=motorcycle()
car.go()
motorcycle.go()