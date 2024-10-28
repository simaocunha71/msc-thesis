def compare_one(a, b):
    if a == b:
        return None
    elif isinstance(a, str):
        return max(a, b, key=float)
    elif isinstance(b, str):
        return max(a, b, key=float)
    else:
        return max(a, b)

print(compare_one(1, 2.5))  # 2.5
print(compare_one(1, "2,3"))  # "2,3"
print(compare_one("5,1", "6"))  # "6"
print(compare_one("1", 1))  # None