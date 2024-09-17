def is_Sub_Array(arr1, arr2):
    if set(arr2).issubset(set(arr1)):
        return True
    return False