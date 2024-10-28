
def right_insertion(sorted_list, value):
    if value > sorted_list[-1]:
        return len(sorted_list)
    if value < sorted_list[0]:
        return 0
    for i in range(len(sorted_list)):
        if sorted_list[i] > value:
            return i
    return len(sorted_list)


