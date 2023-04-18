'''
Justin Klemick
Week 8 Lab
Module containing Vehicle class
'''


class Vehicle:
    '''Vehicle class'''

    def __init__(self, horsepower):
        '''Vehicle constructor'''
        self._horsepower = horsepower

    def get_horsepower(self):
        '''Function to get horsepower'''
        return self._horsepower

    def get_classification(self):
        '''Function to determine classification'''
        if self._horsepower <= 130:
            return 'Compact Vehicle'
        if self._horsepower <= 170:
            return 'Midsize Vehicle'
        return 'Fullsize Vehicle'

class Car(Vehicle):
    '''Car class'''
    def __init__(self, horsepower, doors):
        '''Car constructor'''
        super().__init__(horsepower)
        self.set_doors(doors)

    def set_doors(self, doors):
        '''Function to set doors'''
        self._doors = doors

    def get_classification(self):
        '''Function to determine classification'''
        classification = super().get_classification().split()[0]
        if self._doors == 4:
            classification += 'Sedan'
        elif self._doors == 2:
            classification += 'Coupe'
        else:
            classification += 'Car'
        return classification

class Truck(Vehicle):
    '''Truck class'''

    def __init__(self, horsepower, drive):
        '''Truck constructor'''
        super().__init__(horsepower)
        self.set_drive(drive)

    def set_drive(self, drive):
        '''Function to set drive'''
        self._drive = drive

    def get_drive(self):
        '''Function to get drive'''
        return self._drive

    def get_classification(self):
        '''Function to determine classification'''
        return super().get_classification().split()[0] + '' + self._drive + 'Truck'
        
def test_vehicle():
    '''Test Vehicle class'''
    vehicle1 = Vehicle(100)
    assert vehicle1.get_horsepower() == 100
    assert vehicle1.get_classification() == 'Compact Vehicle'
    vehicle2 = Vehicle(150)
    assert vehicle2.get_horsepower == 150
    assert vehicle2.get_classification == 'Midsize Vehicle'
    vehicle3 = Vehicle(200)
    assert vehicle3.get_horsepower == 200
    assert vehicle3.get_classification == 'Fullsize Vehicle'

def test_car():
    '''Test car class'''
    car1 = Car(100, 2)
    assert car1.get_horsepower() == 100
    assert car1.get_classification() == 'Compact Coupe'
    car2 = Car(100, 4)
    assert car2.get_horsepower() == 100
    assert car2.get_classification() == 'Compact Sedan'
    car3 = Car(150, 2)
    assert car3.get_horsepower() == 150
    assert car3.get_classification() == 'Midsize Coupe'
    car4 = Car(150, 4)
    assert car4.get_horsepower() == 150
    assert car4.get_classification() == 'Midsize Sedan'
    car5 = Car(200, 2)
    assert car5.get_horsepower() == 200
    assert car5.get_classification() == 'Fullsize Coupe'
    car6 = Car(200, 4)
    assert car6.get_horsepower() == 200
    assert car6.get_classification() == 'Fullsize Sedan'

def test_truck():
    '''Test Truck class'''
    truck1 = Truck(100, 'RWD')
    assert truck1.get_horsepower() == 100
    assert truck1.get_classification() == 'Compact RWD Truck'
    truck2 = Truck(100, '4x4')
    assert truck2.get_horsepower() == 100
    assert truck2.get_classification() == 'Compact 4x4 Truck'
    truck3 = Truck(150, 'RWD')
    assert truck3.get_horsepower() == 150
    assert truck3.get_classification() == 'Midsize RWD Truck'
    truck4 = Truck(150, '4x4')
    assert truck4.get_horsepower() == 150
    assert truck4.get_classification() == 'Midsize 4x4 Truck'
    truck5 = Truck(200, 'RWD')
    assert truck5.get_horsepower() == 200
    assert truck5.get_classification() == 'Fullsize RWD Truck'
    truck6 = Truck(200, '4x4')
    assert truck6.get_horsepower() == 200
    assert truck6.get_classification() == 'Fullsize 4x4 Truck'

if __name__ == 'main':
    test_vehicle()
    test_car()
    test_truck()
