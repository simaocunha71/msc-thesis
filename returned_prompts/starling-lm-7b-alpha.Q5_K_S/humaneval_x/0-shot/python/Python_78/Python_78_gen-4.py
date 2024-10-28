
def hex_key(num):
    prime_hex_dict = {
        "2": 2, "3": 3, "5": 5, "7": 7, "B": 11, "D": 13,
        "A": 10, "C": 9, "E": 8, "F": 7
    }

    hex_num = [str(x) for x in num]

    count = 0
    for i in hex_num:
        if prime_hex_dict[i] == int(i):
            count += 1

    return count


# Tests
print(hex_key("AB"))  # 1
print(hex_key("1077E"))  # 2
print(hex_key("ABED1A33"))  # 4
print(hex_key("123456789ABCDEF0"))  # 6
print(hex_key("2020"))  # 2
print(hex_key(""))  # 0


























```