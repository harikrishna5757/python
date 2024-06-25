class Parent:
    def __init__(self, asserts):
        self.asserts = asserts

    def current_asserts(self):
        pass


class Child1(Parent):
    def current_asserts(self):
        return self.asserts + 200


class Child2(Parent):
    def current_asserts(self):
        return self.asserts + 250


child1 = Child1(100)
child2 = Child2(100)
print(child1.current_asserts())
print(child2.current_asserts())
