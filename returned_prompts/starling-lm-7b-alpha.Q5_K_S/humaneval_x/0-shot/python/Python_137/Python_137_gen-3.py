
def compare_one(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif isinstance(a, str) and isinstance(b, str):
        if a.replace(',', '') > b.replace(',', ''):
            return a.replace(',', '')
        elif a.replace(',', '') < b.replace(',', ''):
            return b.replace(',', '')
        else:
            return None
    elif isinstance(a, (int, float)) and isinstance(b, str):
        if a > float(b.replace(',', '')):
            return a
        elif a < float(b.replace(',', '')):
            return float(b.replace(',', ''))
        else:
            return None
    elif isinstance(a, str) and isinstance(b, (int, float)):
        if float(a.replace(',', '')) > b:
            return float(a.replace(',', ''))
        elif float(a.replace(',', '')) < b:
            return b
        else:
            return None
    else:
        return "Invalid Input"


# Test Cases
print(compare_one(1, 2.5))  # 2.5
print(compare_one(1, "2,3"))  # "2,3"
print(compare_one("5,1", "6"))  # "6"
print(compare_one("1", 1))  # None
print(compare_one(1, "1"))  # None
print(compare_one(1, "1,"))  # "1,"
print(compare_one(1.0, "1"))  # None
print(compare_one(1.0, "1,"))  # "1,"
print(compare_one(1.0, "1.0"))  # None
print(compare_one(1.0, "1,0"))  # "1,0"
print(compare_one(1.0,