class Shape:
    def __init__(self, colour, cost):
        self.colour = colour
        self.cost = cost
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, colour, cost):
        super().__init__(colour, cost)
        self.__height = 0
        self.__width = 0
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, n):
        if n <= 0:
            raise ValueError("height must be greater than 0")
        self.__height = n
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, n):
        if n <= 0:
            raise ValueError("width must be greater than 0")
        self.__width = n
    def area(self):
        self.height = int(input("enter the height: "))
        self.width = int(input("enter the width: "))
        self.tarea = self.height * self.width
        print(f"the area is {self.tarea}")
    def cost_square(self):
        total = self.tarea * self.cost
        print(f"total cost is {total}")

class Circle(Shape):
    def __init__(self, colour, cost):
        super().__init__(colour, cost)
        self.__radius = 0
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, n):
        if n <= 0:
            raise ValueError("radius must be greater than 0")
        self.__radius = n
    def area(self):
        self.radius = int(input("enter the radius: "))
        self.tarea = 3.14159 * (self.radius ** 2)
        print(f"the area is {self.tarea}")
    def cost_square(self):
        total = self.tarea * self.cost
        print(f"total cost is {total}")