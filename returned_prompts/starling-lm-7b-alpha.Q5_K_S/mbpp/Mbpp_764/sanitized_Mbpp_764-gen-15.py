def number_ctr(string: str):
    count = 0
    for i in string:
        if i.isdigit():
            count += 1
    return count