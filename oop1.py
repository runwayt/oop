class Car(object):
    def __init__(self, number: str, model: str, milleage: int):
        self.number = number
        self.model = model
        self.milleage = milleage

    def __repr__(self):
        return "<Car number:%s, model:%s, milleage:%s>" % (self.number, self.model, self.milleage)

    def __str__(self):
        return "Car number:%s, model:%s, milleage:%s" % (self.number, self.model, self.milleage)

    def number(self):
        return self.number

    def model(self):
        return self.model

    def milleage(self):
        return self.milleage


class AutoService(object):
    def __init__(self, name: str):
        self.name = name
        self.cars = list()
    
    def addCar(self, car: Car):
        self.cars.append(car)

    def cars(self):
        return self.cars

    def name(self):
        return self.name


service = AutoService('Garage')
chev = Car('AA0000AA', 'Chevrolet Camaro', 20000)
service.addCar(chev)
print(service.cars)