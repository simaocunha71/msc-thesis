
def compare_one(a, b):
    if isinstance(a, str) and isinstance(b, str):
        a_list = a.split(",")
        b_list = b.split(",")
        a_float = float(a_list[0]) + float(a_list[1])
        b_float = float(b_list[0]) + float(b_list[1])
        if a_float == b_float:
            return None
        elif a_float > b_float:
            return a_list[0] + "," + a_list[1]
        else:
            return b_list[0] + "," + b_list[1]
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    elif isinstance(a, str):
        return float(a)
    else:
        return float(b)


# Another solution

def compare_one(a, b):
    if isinstance(a, str):
        a = a.replace(".", ",")
        a_list = a.split(",")
        a_float = float(a_list[0]) + float(a_list[1])
    elif isinstance(b, str):
        b = b.replace(".", ",")
        b_list = b.split(",")
        b_float = float(b_list[0]) + float(b_list[1])
    if a_float == b_float:
        return None
    elif a_float > b_float:
        return a_float
    else:
        return b_float


# Test

print(compare_one(1, 2.5))  # 2.5
print(compare_one(1, "2,3"))  # "2,3"
print(compare_one("5,1", "6"))  # "6"
print(compare_one("1", 1))  # None
























