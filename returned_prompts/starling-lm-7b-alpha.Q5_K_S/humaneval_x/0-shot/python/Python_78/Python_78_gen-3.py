
def hex_key(num):
    hex_dict = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }
    prime_dict = {
        2: True,
        3: True,
        5: True,
        7: True,
        11: True,
        13: True
    }
    count = 0
    for i in num:
        if i in prime_dict:
            count += 1
        else:
            if hex_dict[i] in prime_dict:
                count += 1
    return count

# Testing:
print(hex_key("AB"))  # 1
print(hex_key("1077E"))  # 2
print(hex_key("ABED1A33"))  # 4
print(hex_key("123456789ABCDEF0"))  # 6
print(hex_key("2020"))  # 2

































































































































































