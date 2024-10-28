def is_Sub_Array(sub_arr, arr):
    return all(x in arr for x in sub_arr)
