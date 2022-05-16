from dataclasses import dataclass

# only present in Python 3.8+
# caches the property value so that it doesn't need to be computed at runtime again and again
from functools import cached_property


@dataclass
class Employee:
    first_name: str
    last_name: str
    age: int

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @name.setter
    def name(self, name):
        self.first_name, self.last_name = name.split(" ")


if __name__ == "__main__":
    emp1 = Employee("Hari", "Krishna", 22)
    print("Before: ", emp1.name)
    emp1.name = "Suyog Dahal"
    print("After: ", emp1.name)
    print("After: ", emp1.first_name)
