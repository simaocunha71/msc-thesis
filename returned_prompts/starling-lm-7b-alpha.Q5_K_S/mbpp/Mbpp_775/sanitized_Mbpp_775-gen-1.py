def odd_position(lst):
    for i in range(len(lst)):
        if i%2 == 0 and lst[i]%2 != 0:
            return False
    return True