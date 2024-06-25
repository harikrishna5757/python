from abc import ABC, abstractmethod


# Abstract class
def normal():
    print("normal method")


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        raise NotImplementedError


n = Shape()
normal()
