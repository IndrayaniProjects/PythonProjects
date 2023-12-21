def factorial(val):
    if type(val) is not int:
        print("Value you are entering is NOT integer")
        return None
    if val<0:
        print("Value you are entering is less than Zero")
        return None
    if val == 0:
         return 1
    return val * factorial(val-1)

print(factorial(5))

      