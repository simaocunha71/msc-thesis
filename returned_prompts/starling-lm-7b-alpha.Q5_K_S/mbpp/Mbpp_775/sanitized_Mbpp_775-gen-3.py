def odd_position(list):
    for i in range(0, len(list), 2):
        if list[i] % 2 != 0:
            return False
    return True