from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name) -> None:
        if not name:
            raise ValueError("Empty name not allowed!")
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, name, length, width) -> None:
        # We should ideally use super to initialize name here so that we can add checks in the abstract class to see if name is empty or not
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length * self.width


rectangle = Rectangle("dsfasd", 5, 4)
print(rectangle.area(), rectangle.name)
