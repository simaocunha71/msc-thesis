import re
def move_num(s):
    letters = []
    numbers = []
    for i in s:
        if i.isalpha():
        # if i.isdigit() == False:
            letters.append(i)
        else:
            numbers.append(i)
    return ''.join(letters+numbers)