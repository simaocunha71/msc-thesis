def number_ctr(string):
    number_count = 0
    for char in string:
        if char.isdigit():
            number_count += 1
    return number_count