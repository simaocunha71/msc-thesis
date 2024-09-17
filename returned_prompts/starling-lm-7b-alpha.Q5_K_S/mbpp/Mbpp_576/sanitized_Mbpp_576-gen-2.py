def is_Sub_Array(list_1, list_2):
    if len(list_1) > len(list_2):
        return False
    j = 0
    for i in range(len(list_1)):
        if list_1[i] == list_2[j]:
            j += 1
        if j == len(list_2):
            return True
    return False