import math

class Square:
    def __init__(self, side):
        self.side = side
        self.circunference = side * 4
        self.field = side * side
    
    def getCircunference(self):
        return(self.circunference)

    def getField(self):
        return(self.field)

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.circunference = math.pi * 2 * radius
        self.field = math.pi * radius * radius
        
    def getCircunference(self):
        return(self.circunference)

    def getField(self):
        return(self.field)
    
class EquilateralTriangle:
    def __init__(self, side):
        self.side = side
        self.circunference = side * 3
        self.field = math.sqrt(3)/4 * side * side
    
    def getCircunference(self):
        return(self.circunference)

    def getField(self):
        return(self.field)

square = Square(5)
print("Field: ", square.getField(), " Perimeter: ", square.getCircunference())
triangle = EquilateralTriangle(5)
print("Field: ", triangle.getField(), " Perimeter: ", triangle.getCircunference())
circle = Circle(5)
print("Field: ", circle.getField(), " Perimeter: ", circle.getCircunference())
square2 = Square(2)
print("Field: ", square2.getField(), " Perimeter: ", square2.getCircunference())
triangle2 = EquilateralTriangle(2)
print("Field: ", triangle2.getField(), " Perimeter: ", triangle2.getCircunference())
circle2 = Circle(2)
print("Field: ", circle2.getField(), " Perimeter: ", circle2.getCircunference())
