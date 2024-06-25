class Tablet:
    def __init__(self, capsule, normal):
        self.__capsule = capsule  # Private attribute
        self.normal = normal

    def get_capsule(self):
        return self.__capsule


acc = Tablet(100, 8)
print(acc.normal)
print(acc.get_capsule())
print(acc.__capsule)
