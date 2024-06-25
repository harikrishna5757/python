class Overloading:
    def sum(self, a, b):
        print(a + b)

    def sum(self, a, b, c):
        print(a + b + c)


Overloading.sum(1, 2)
Overloading.sum(1, 2, 3)
