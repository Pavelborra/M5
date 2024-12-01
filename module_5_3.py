class House:
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
        elif isinstance(other, float):
            return self.number_of_floors == other
        elif isinstance(other, str):
            return str(self) == other
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
        elif isinstance(other, float):
            return self.number_of_floors < other
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other
        elif isinstance(other, float):
            return self.number_of_floors <= other
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other
        elif isinstance(other, float):
            return self.number_of_floors > other
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other
        elif isinstance(other, float):
            return self.number_of_floors >= other
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other
        elif isinstance(other, float):
            return self.number_of_floors != other
        elif isinstance(other, str):
            return str(self) != other
        else:
            return NotImplemented

    def __add__(self, value):
        new_number = self.number_of_floors
        if isinstance(value, House):
            new_number += value.number_of_floors
        elif isinstance(value, int):
            new_number += value
        else:
            return NotImplemented
        return House(self.name, new_number)

    __radd__ = __add__

    def __iadd__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        elif isinstance(value, int):
            self.number_of_floors += value
        else:
            return NotImplemented
        return self

    def __sub__(self, value):
        new_number = self.number_of_floors
        if isinstance(value, House):
            new_number -= value.number_of_floors
        elif isinstance(value, int):
            new_number -= value
        else:
            return NotImplemented
        return House(self.name, new_number)

    __rsub__ = __sub__

    def __isub__(self, value):
        if isinstance(value, House):
            self.number_of_floors -= value.number_of_floors
        elif isinstance(value, int):
            self.number_of_floors -= value
        else:
            return NotImplemented
        return self

    def __mul__(self, value):
        new_number = self.number_of_floors
        if isinstance(value, House):
            new_number *= value.number_of_floors
        elif isinstance(value, int):
            new_number *= value
        else:
            return NotImplemented
        return House(self.name, new_number)

    __rmul__ = __mul__

    def __imul__(self, value):
        if isinstance(value, House):
            self.number_of_floors *= value.number_of_floors
        elif isinstance(value, int):
            self.number_of_floors *= value
        else:
            return NotImplemented
        return self

    def __floordiv__(self, value):
        new_number = self.number_of_floors
        if isinstance(value, House):
            new_number //= value.number_of_floors
        elif isinstance(value, int):
            new_number //= value
        else:
            return NotImplemented
        return House(self.name, new_number)

    __rfloordiv__ = __floordiv__

    def __ifloordiv__(self, value):
        if isinstance(value, House):
            self.number_of_floors //= value.number_of_floors
        elif isinstance(value, int):
            self.number_of_floors //= value
        else:
            return NotImplemented
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__