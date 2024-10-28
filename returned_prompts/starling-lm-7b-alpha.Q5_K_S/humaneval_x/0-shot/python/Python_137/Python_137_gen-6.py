
def compare_one(a, b):
    if isinstance(a, str):
        a = float(a.replace(",", "."))
    if isinstance(b, str):
        b = float(b.replace(",", "."))
    if a == b:
        return None
    elif isinstance(a, float) and isinstance(b, float):
        if a > b:
            return a
        else:
            return b
    elif isinstance(a, int) and isinstance(b, int):
        if a > b:
            return a
        else:
            return b
    elif isinstance(a, str):
        return a
    else:
        return b


# Test
print(compare_one(1, 2.5))  # 2.5
print(compare_one(1, "2,3"))  # "2,3"
print(compare_one("5,1", "6"))  # "6"
print(compare_one("1", 1))  # None
















# My Code
# def compare_one(a, b):
#     if isinstance(a, str) and isinstance(b, str):
#         if a > b:
#             return a
#         else:
#             return b
#     elif isinstance(a, float) and isinstance(b, float):
#         if a > b:
#             return a
#         else:
#             return b
#     elif isinstance(a, int) and isinstance(b, int):
#         if a > b:
#             return a
#         else:
#             return b
#     else:
#         return None

# Test
# print(compare_one(1, 2.5))  # 2.5
# print(compare_one(1, "2,3"))  # "2,3"
# print(compare_one("5,1", "6"))  # "6"
# print(compare_one("1", 1))  # None























# Solution
def compare_