# WAP for area and perimeter of the triangle using class and objects
import math
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return 'the perimeter of the triangle is: {}'.format(a+b+c)

    def area(self):
        # using Heron's Formula
        s = (a + b + c)/2  # semi perimeter
        areaT = math.sqrt(s*(s-a)*(s-b)*(s-c))
        return 'the area of the triangle is: {}'.format(areaT)

a = int(input('enter first side: '))
b = int(input('enter second side: '))
c = int(input('enter third side: '))
triangle = Triangle(a,b,c)
print(triangle.perimeter())
print(triangle.area())
