class Triangle:
    def __init__(self, height, base):
        self.height = height
        self.base = base
    def area (self):
        return (self.height * self.base)/2

triangle1 = Triangle(30,4)
print("Area of triangle is: {}".format(triangle1.area()))