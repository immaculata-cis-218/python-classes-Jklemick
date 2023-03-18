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
            return 'Compact'
        if self._horsepower <= 170:
            return 'Midsize'
        return 'Fullsize'

def test_vehicle():
    '''Test Vehicle class'''
    vehicle1 = Vehicle(100)
    assert vehicle1.get_horsepower() == 100
    assert vehicle1.get_classification() == 'Compact'
    vehicle2 = Vehicle(150)
    assert vehicle2.get_horsepower == 150
    assert vehicle2.get_classification == 'Midsize'
    vehicle3 = Vehicle(200)
    assert vehicle3.get_horsepower == 200
    assert vehicle3.get_classification == 'Fullsize'

if __name__ == 'main':
    test_vehicle()
