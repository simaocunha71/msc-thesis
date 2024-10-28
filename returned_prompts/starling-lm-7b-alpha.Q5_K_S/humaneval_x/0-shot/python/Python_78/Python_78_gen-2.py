
def hex_key(num):
    hex_dict = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    hex_list = [hex_dict[char] for char in num]
    count = 0
    for i in hex_list:
        if i in [2, 3, 5, 7, 11, 13]:
            count += 1
    return count

# print(hex_key("AB")) # 1
# print(hex_key("1077E")) #