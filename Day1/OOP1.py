
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def test(self):
        print(self.x)

    def __add__(self, other):
        print(self.x)
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"This point has the values {self.x} and {self.y}"

def main():
    p1 = Point(2,3)
    p2 = Point(3,4)

    p3 = p1 + p2
    p4 = p3 + p2 + p1
    print(p4)



    #p1.__x = 99
    #print(p1.__x)
    #p1.test()
    
if __name__ == '__main__':
    main()