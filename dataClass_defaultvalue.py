#using data class default values

from dataclasses import dataclass, field
import random

@dataclass
class Book:

    def price_func():
        return float(random.randrange(1,1000))
    # you can define values when atttributes are declared
    title : str = "No title"
    author : str = "No author"
    pages : int = 0
    price : float = field(default_factory=price_func)

   

''''b1 = Book()
print (b1)'''

b2 = Book("War and Peace ", "Leo Tolstoy",1225)
b3 = Book("The catcher in the Ray", "JD Salinger", 560)

print(b2)
print(b3)

