
def move_num(s):
    non_digit = ""
    for i in s:
        if not i.isdigit():
            non_digit += i
    for i in s[::-1]:
        if i.isdigit():
            non_digit += i
    return non_digit


