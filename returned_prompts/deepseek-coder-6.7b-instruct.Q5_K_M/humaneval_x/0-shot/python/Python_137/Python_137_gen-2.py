
def compare_one(a, b):
    if isinstance(a, str):
        a = float(a.replace(',', '.'))
    if isinstance(b, str):
        b = float(b.replace(',', '.'))

    if a == b:
        return None
    elif isinstance(a, float) or isinstance(b, float):
        return max(a, b, key=float)
    else:
        return max(a, b)

print(compare_one(1, 2.5))  # ➞ 2.5
print(compare_one(1, "2,3"))  # ➞ "2,3"
print(compare_one("5,1", "6"))  # ➞ "6"
print(compare_one("1", 1))  # ➞ None


# ➞ 2.5
# ➞ "2,3"
# ➞ "6"
# ➞ None

In the function above, we first check if either a or b is a string. If so, we replace the comma with a dot and convert it to a float.

Then, we check if a and b are floats. If either of them is a float, we return the max of a and b with the key as float to get the correct comparison even if one of them are ints.

If neither a nor b are floats, we just return the max of a and b.
"""


def compare_one(a, b):
    if isinstance(a, str):
        a = float(a.replace(',', '.'))
    if isinstance(b, str):
        b = float(b.replace(',', '.'))

    if a == b:
        return None
    elif isinstance(a, float) or isinstance(b, float):
        return max(a, b, key=float)
    else:
        return max(a, b)


print(compare_one(1, 2.5))  # ➞ 2.5
print(compare_one(1, "2,3