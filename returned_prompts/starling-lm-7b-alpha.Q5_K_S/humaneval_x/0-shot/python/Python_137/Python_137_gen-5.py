
def compare_one(a, b):
    # Convert string to float
    if isinstance(a, str):
        a = float(a.replace(',', ''))
    if isinstance(b, str):
        b = float(b.replace(',', ''))
    # Compare and return
    if a == b:
        return None
    elif type(a) == type(b):
        if a > b:
            return a
        else:
            return b
    elif type(a) == int:
        return b
    elif type(b) == int:
        return a
    elif type(a) == float:
        return b
    elif type(b) == float:
        return a

# Test
print(compare_one(1, 2.5))  # 2.5
print(compare_one(1, "2,3"))  # "2,3"
print(compare_one("5,1", "6"))  # "6"
print(compare_one("1", 1))  # None







def compare_one(a, b):
    # Convert string to float
    if isinstance(a, str):
        a = float(a.replace(',', ''))
    if isinstance(b, str):
        b = float(b.replace(',', ''))
    # Compare and return
    if a == b:
        return None
    elif type(a) == type(b):
        if a > b:
            return a
        else:
            return b
    elif type(a) == int:
        return b
    elif type(b) == int:
        return a
    elif type(a) == float:
        return b
    elif type(b) == float:
        return a

# Test
print(compare_one(1, 2.5))  # 2.5
print(compare_one(1, "2,3"))  # "2,3"
print(compare_one("5,1", "6"))  # "6"
print(compare_one("1", 1))  # None










