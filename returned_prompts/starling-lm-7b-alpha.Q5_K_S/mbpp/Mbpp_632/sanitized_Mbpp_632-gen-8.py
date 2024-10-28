def move_zero(list):
    zeros = []
    for i in range(len(list)):
        if list[i] != 0:
            print(list[i])
        else:
            zeros.append(list[i])
    return zeros + list