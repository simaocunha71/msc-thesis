    if type(a) == type(b) and type(a) in [int, float]:
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif type(a) == str and type(b) == str:
        a = float(a.replace(",", "."))
        b = float(b.replace(",", "."))
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    else:
        return None
    # handle the case where a and b are of different types
    # if a is an int and b is a float, convert a to a float
    # then compare, and return the larger value
    # if a is a float and b is an int, convert b to a float and compare
    # if a is a string and b is not, convert b to a string and compare
    # if a is not a string and b is, convert a to a string and compare
    # if a and b are of different types, return None
    # if a is larger, return a, otherwise return b
    # if the values are equal, return None
    # if a is an int and b is a float, convert a to a float and compare
    # if a is a float and b is an int, convert b to a float and compare
    # if a is a string and b is not, convert b to a string and compare
    # if a is not a string and b is, convert a to a string and compare
    # if a and b are of different types, return None
    # if a is larger, return a, otherwise return b
    # if the values are equal, return None
    # if a is an int and b is a float, convert a to a float and compare
    # if a is a float and b is an int, convert b to a float and compare
    # if a is a string and b is not, convert b to a string and compare
    # if a is not a string and b is, convert a to a string and compare
    # if a and b are of different types, return None
    # if a is larger, return a, otherwise return b
    # if the values are equal, return None
    # if a is an int and b is a float, convert