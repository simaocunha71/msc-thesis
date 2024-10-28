
def compare_one(a, b):
    if type(a) == str:
        a = float(a.replace(",", "."))
    if type(b) == str:
        b = float(b.replace(",", "."))

    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None

print(compare_one(1, 2.5)) # ➞ 2.5
print(compare_one(1, "2,3")) # ➞ "2.3"
print(compare_one("5,1", "6")) # ➞ "6"
print(compare_one("1", 1)) # ➞ None


# --------------------- 2nd approach -------------------------

def compare_one(a, b):
    a = float(str(a).replace(",", ".")) if type(a) in [str, float] else a
    b = float(str(b).replace(",", ".")) if type(b) in [str, float] else b

    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None

print(compare_one(1, 2.5)) # ➞ 2.5
print(compare_one(1, "2,3")) # ➞ "2.3"
print(compare_one("5,1", "6")) # ➞ "6"
print(compare_one("1", 1)) # ➞ None

# --------------------- 3rd approach -------------------------

def compare_one(a, b):
    a = a if isinstance(a, (int, float)) else float(str(a).replace(",", "."))
    b = b if isinstance(b, (int, float)) else float(str(b).replace(",", "."))

    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None

print(compare_one(1, 2.5