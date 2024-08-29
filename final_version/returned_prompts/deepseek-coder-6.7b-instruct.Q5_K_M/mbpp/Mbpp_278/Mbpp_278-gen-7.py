
def count_first_elements(tup):
    count = 0
    for i in tup:
        if isinstance(i, tuple):
            break
        count += 1
    return count

assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3

#