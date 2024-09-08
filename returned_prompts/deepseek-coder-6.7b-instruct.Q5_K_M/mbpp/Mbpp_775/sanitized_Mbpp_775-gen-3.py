def odd_position(lst):
    for i in range(len(lst)):
        if i % 2 != 0:
            if lst[i] % 2 == 0:
                return False
    return True