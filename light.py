class Car:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f"{self.name} is moving.")

    def stop(self):
        print(f"{self.name} has stopped.")

    def turn(self, direction):
        print(f"{self.name} turned {direction}.")

class TownCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)

class SportCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)

class WorkCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

town_car = TownCar("Toyota", "Blue", 120)
sport_car = SportCar("Ferrari", "Red", 200)
work_car = WorkCar("Ford", "White", 100)
police_car = PoliceCar("Dodge", "Black", 150)

town_car.go()
sport_car.turn("right")
work_car.stop()
police_car.go()