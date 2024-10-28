def odd_position(l):
    if len(l) % 2 == 0:
        return False
    for i in range(0, len(l)-1, 2):
        if l[i] % 2 == 0 or l[i+1] % 2 == 0:
            return False
    return True