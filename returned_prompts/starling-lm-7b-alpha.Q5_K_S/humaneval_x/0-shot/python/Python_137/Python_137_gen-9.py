
def compare_one(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    elif isinstance(a, (str)) and isinstance(b, (str)):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    else:
        return None


# Test cases
print(compare_one(1, 2.5))  # Expected: 2.5
print(compare_one(1, "2,3"))  # Expected: "2,3"
print(compare_one("5,1", "6"))  # Expected: "6"
print(compare_one("1", 1))  # Expected: None





def compare_two(a, b):
    """
    Create a function that takes two integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    elif isinstance(a, (str)) and isinstance(b, (str)):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    else:
        return None


# Test cases
print(compare_two(1, 2.5))  # Expected: 2.5
print(compare_two(1, "2,3"))  # Expected: "2,3"
print(compare_two("5,1", "6"))  # Expected: "6"
print(compare_two("1", 1))  # Expected: None





def compare_three(a, b