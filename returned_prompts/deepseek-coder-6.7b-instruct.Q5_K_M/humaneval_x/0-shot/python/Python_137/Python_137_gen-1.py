
def compare_one(a, b):
    if type(a) == str:
        a = float(a.replace(',', '.'))
    if type(b) == str:
        b = float(b.replace(',', '.'))

    if a == b:
        return None
    else:
        return max(a, b)

print(compare_one(1, 2.5))  # ➞ 2.5
print(compare_one(1, "2,3"))  # ➞ "2,3"
print(compare_one("5,1", "6"))  # ➞ "6"
print(compare_one("1", 1))  # ➞ None

def compare_one(a, b):
    if isinstance(a, str):
        a = float(a.replace('.', '').replace(',', '.'))
    if isinstance(b, str):
        b = float(b.replace('.', '').replace(',', '.'))
    try:
        return max(a, b) if a != b else None
    except ValueError:
        return None

print(compare_one(1, 2.5))  # ➞ 2.5
print(compare_one(1, "2,3"))  # ➞ "2,3"
print(compare_one("5,1", "6"))  # ➞ "6"
print(compare_one("1", 1))  # ➞ None

def compare_one(a, b):
    if isinstance(a, str):
        a = float(a.replace(',', '.'))
    if isinstance(b, str):
        b = float(b.replace(',', '.'))
    return max(a, b) if a != b else None

print(compare_one(1, 2.5))  # ➞ 2.5
print(compare_one(1, "2,3"))  # ➞ "2,3"
print(compare_one("5,1", "6")) 