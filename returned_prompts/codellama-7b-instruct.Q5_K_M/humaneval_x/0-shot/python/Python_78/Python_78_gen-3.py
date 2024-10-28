
def hex_key(num):
    if num == "":
        return 0
    if num[0] in "2468" or num[0] == "A" or num[0] == "B" or num[0] == "D":
        return 1
    if num[0] == "1" or num[0] == "3" or num[0] == "5" or num[0] == "7":
        return 2
    return 0
