class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"X = {self.x} and Y = {self.y}"

print(Point(10, -2))
