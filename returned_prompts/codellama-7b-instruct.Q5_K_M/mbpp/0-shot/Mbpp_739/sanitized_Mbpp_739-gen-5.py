def find_Index(n):
    number = 1
    while len(str(number)) < n:
        number += 1
    return len(str(number))