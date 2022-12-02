import math

class Callback:
    def __init__(self):
        pass

    def debug(self):
        print('We Are in operations.py')

    def debug_odom(self, valX, valY):
        print('ODOM.X = ' + str(valX) + "ODOM.Y = " + str(valY))

    def sqrt(self, val):
        return math.sqrt(val)
