
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """

    # print(type(a))
    if (type(b) == type(a)):
        return eval(str(a)(b).strip())
    
    elif (type(b) != type(a)):
        return a

def compare_two(a, b):
    """
    Create a function that takes an array of integers or floating point numbers.
    Return the largest value in its given variable type for each array item.
    Return None if any values are equal or no elements exist.
    Note: If a real number is represented as a string, the floating point might be . or ,
    
    compare_two(["5","3"]) ➞ ["5", "3"]
    """

    # print(type(a))
    if (type(b) == type(a)):
        return eval(str(a)(b).strip())

    elif(type(a) != type(b)):
        return a
    
def compare_three(num1, num2):
    """
    Create a function that takes an array of integers or floating point numbers.
    Return the largest value in its given variable type for each array item.
    Return None if any values are equal or no elements exist.
    Note: If a real number is represented as a string, the floating point might be . or ,
    
    compare_two(["5","3"]) ➞ ["5", "3"]"""

# print(type(num1))
# print(type(num2))
if (type(