def is_Sub_Array(list_1, list_2):
    if len(list_1) > len(list_2):
        return False
    else:
        for i in range(len(list_1)):
            if list_1[i] not in list_2:
                return False
        return True