def is_Sub_Array(sub_array, array):
    if len(sub_array) > len(array):
        return False
    for i in range(len(array) - len(sub_array) + 1):
        if array[i:i+len(sub_array)] == sub_array:
            return True
    return False