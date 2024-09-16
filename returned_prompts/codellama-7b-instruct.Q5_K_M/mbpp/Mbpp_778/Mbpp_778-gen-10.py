def pack_consecutive_duplicates(my_list):
    my_list = sorted(my_list)
    packed = []
    current = []
    for i in range(len(my_list)):
        if i == 0:
            current.append(my_list[i])
        else:
            if my_list[i] == my_list[i-1]:
                current.append(my_list[i])
            else:
                packed.append(current)
                current = [my_list[i]]
    packed.append(current)
    return packed

