def is_Sub_Array(sub_array, main_array):
    if len(sub_array) > len(main_array):
        return False
    sub_array_index = 0
    for i in range(len(main_array)):
        if main_array[i] == sub_array[sub_array_index]:
            sub_array_index += 1
        if sub_array_index == len(sub_array):
            return True
    return False