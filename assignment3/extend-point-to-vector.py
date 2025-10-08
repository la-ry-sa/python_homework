from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def distance(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return sqrt(dx**2 + dy**2)

class Vector(Point):

    def __str__(self):
        return f"<{self.x}, {self.y}>"
    
    def __add__(self, other):
        new_x = other.x + self.x
        new_y = other.y + self.y
        return Vector(new_x, new_y)


if __name__ == "__main__":

    test_point = Point(4, 7)
    test_vector = Vector(10, -6)

    print(test_point)
    print(test_vector)
    print(test_point == test_vector)

    print(test_point.distance(test_vector))

    new_vector = Vector(3, 16)

    vector_sum = test_vector + new_vector
    print(vector_sum)