def count_first_elements(t):
    counter = 0
    for elem in t:
        if isinstance(elem, tuple):
            counter += 1
    return counter
t = (1, 5, 7, (4, 6), 10)