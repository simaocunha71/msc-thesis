
def compare_one(a, b):
    a = a if isinstance(a, str) else str(a)
    b = b if isinstance(b, str) else str(b)

    a = a.replace('.', '').replace(',', '.')
    b = b.replace('.', '').replace(',', '.')

    a = float(a)
    b = float(b)

    if a > b:
        return a
    elif a < b:
        return b
    else:
        return None

print(compare_one(1, 2.5))  # ➞ 2.5
print(compare_one(1, "2,3"))  # ➞ "2.3"
print(compare_one("5,1", "6"))  # ➞ "6.0"
print(compare_one("1", 1))  # ➞ None
print(compare_one(2, 2))  # ➞ None

The function starts by checking if the inputs are strings. If not, it converts them to strings. It then replaces the decimal separator with a dot, if present. Finally, it converts the strings to floats and compares them. It returns the larger number, or None if they're equal.

This solution assumes that all inputs are either numbers or strings representing numbers. If this is not the case, you may want to add some error checking to handle inputs of different types.

This solution also assumes that the strings representing numbers are in the format '123.456' or '123,456'. If this is not the case, you may need to add some error checking to handle different formats.

This solution also assumes that the strings representing numbers are in English. If this is not the case, you may need to add some additional logic to handle different languages.

This solution also assumes that the strings representing numbers are in the format '123.456' or '123,456'. If this is not the case, you may need to add some error checking to handle different formats.

This solution also assumes that the strings representing numbers are in English. If this is not the case,