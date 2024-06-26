class Tablet:
    def __init__(self, capsule, normal):
        self.__capsule = capsule  # Private attribute
        self.normal = normal

    def __get_capsule(self):
        return self.__capsule

    def new(self):
        return self.__get_capsule()


acc = Tablet(100, 8)
print(acc.normal)
print(acc.new())
print(acc.__capsule)
