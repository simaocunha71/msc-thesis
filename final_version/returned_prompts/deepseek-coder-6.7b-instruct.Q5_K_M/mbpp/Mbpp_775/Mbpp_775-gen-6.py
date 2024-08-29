def odd_position(lst):
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            return False
    return True

print(odd_position([2,1,4,3,6,7,6,3]))

# Q2
