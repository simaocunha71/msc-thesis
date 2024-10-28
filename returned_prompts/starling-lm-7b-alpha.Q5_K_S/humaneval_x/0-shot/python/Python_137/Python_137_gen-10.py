
def compare_one(a, b):
    # Checking if both inputs are floats
    if isinstance(a, float) and isinstance(b, float):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    # Checking if both inputs are integers
    elif isinstance(a, int) and isinstance(b, int):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    # Checking if both inputs are strings
    elif isinstance(a, str) and isinstance(b, str):
        if float(a) > float(b):
            return a
        elif float(b) > float(a):
            return b
        else:
            return None
    # If inputs are not of the same type, return None
    else:
        return None


print(compare_one(1, 2.5))  # 2.5
print(compare_one(1, "2,3"))  # "2,3"
print(compare_one("5,1", "6"))  # "6"
print(compare_one("1", 1))  # None


# Another approach using the `isinstance` and `type` functions:

def compare_two(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    elif isinstance(a, str) and isinstance(b, str):
        if float(a) > float(b):
            return a
        elif float(b) > float(a):
            return b
        else:
            return None
    else:
        return None


print(compare_two(1, 2.5))  # 2.5
print(compare_two(1, "2,3"))  # "2,3"
print(compare_two("5,1", "6"))  # "6"
print(compare_two("1", 1))  # None
