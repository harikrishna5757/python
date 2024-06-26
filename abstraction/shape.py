from abc import ABC, abstractmethod


# Abstract class
def normal():
    print("normal method")


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        return NotImplementedError


# n = Shape()
