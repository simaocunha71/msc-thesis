"""
You can use the isinstance function to check if all the elements in tuple have same data type or not.

Here is the Python code to check if all elements in a tuple are of same type:

def check_type(tup):
    return all(isinstance(i, type(tup[0])) for i in tup)

In the above code, the all() function will return true if all elements are true, and false if at least one element is false.

Here is how you can use the function:

tup = (5, 6, 7, 3, 5, 6)
print(check_type(tup)) # prints: True
"""

from typing import Tuple

def check_type(tup: Tuple) -> bool:
    return all(isinstance(i, type(tup[0])) for i in tup)

def main():
    tup = (5, 6, 7, 3, 5, 6)
    print(check_type(tup)) # prints: True

if __name__ == "__main__":
    main()

# The isinstance function will return true if the element is of the specified type, otherwise it will return false.
# The all function will return true if all elements are true, and false if at least one element is false.
# The check_type function will return true if all elements in the tuple are of the same type, otherwise it will return false.
# The main function is used to test the check_type function with a sample tuple.
# The print function is used to print the result of the check_type function.

"""
The code defines a function called check_type that takes a tuple as an argument and returns True if all elements in the tuple are of the same type, otherwise it returns False.

The function uses the all function to check if all elements in the tuple are of the same type. The all function returns True if all elements in the tuple are True, otherwise it returns False.

The function uses the isinstance function to check if an element is of a certain type. The isinstance function returns True if the element is of the specified type, otherwise it returns False.

The function uses a generator expression to check if all elements in the tuple are of the same