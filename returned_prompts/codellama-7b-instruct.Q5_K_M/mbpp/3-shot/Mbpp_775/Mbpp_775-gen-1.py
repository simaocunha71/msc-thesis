
def odd_position(my_list):
    for i, x in enumerate(my_list):
        if i % 2 == 1 and x % 2 == 0:
            return False
    return True


