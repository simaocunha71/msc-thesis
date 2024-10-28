def count_first_elements(t):
    count = 0
    for element in t:
        if isinstance(element, tuple):
            count += 1
    return count