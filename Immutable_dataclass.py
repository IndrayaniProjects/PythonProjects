#Creating immutable dataclass

from dataclasses import dataclass

@dataclass(frozen = True) # frozen makes class immutable
class ImmutableClass:
    value1: str= "value 1"
    value2: int = 0

    def some_func(self, newval):
        self.value2 = newval

obj = ImmutableClass("My value", 40)
print(obj.value1,obj.value2)

# Trying to modify the value throws exception
obj.value1 = "Another Value"
print(obj.value1)

obj.some_func(20)