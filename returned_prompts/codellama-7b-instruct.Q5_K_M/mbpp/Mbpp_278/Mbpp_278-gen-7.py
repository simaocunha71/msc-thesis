
def count_first_elements(tup: tuple) -> int:
    count = 0
    for elem in tup:
        if isinstance(elem, tuple):
            break
        count += 1
    return count


