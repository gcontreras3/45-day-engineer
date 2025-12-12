# Demonstrate try/except/finally

try:
    x = int(input("Enter a number: "))
    print("You entered:", x)
except ValueError:
    print("That's not a valid number!")
finally:
    print("End of input")

# Custom exception

class CustomError(Exception):
    pass
def check_positive(num):
    if num < 0:
        raise CustomError("Number must be positive!")
    return num
