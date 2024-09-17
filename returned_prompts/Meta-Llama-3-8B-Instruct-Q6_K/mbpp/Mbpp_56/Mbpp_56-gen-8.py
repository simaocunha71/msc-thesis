```
def check(n):
    reverse = int(str(n)[::-1])
    return n == 2*reverse - 1
``` 

This function works by first reversing the input number. It does this by converting the number to a string, reversing the string using slicing (`[::-1]`), and then converting the result back to an integer. It then checks if the original number is equal to twice its reverse minus one. 

The unit test `assert check(70) == False` helps to clarify the expected behavior of the function. It indicates that the function should return `False` when the input is 70, which means that 70 is not one less than twice its reverse. 

The function will return `True` for inputs that are one less than twice their reverse, and `False` for all other inputs. For example, `check(169)` would return `True` because 169 is one less than twice its reverse (169 is equal to 2*61 - 1). 

Note that this function assumes that the input is a non-negative integer. If the input can be negative or a non-integer, additional error checking would be needed. 