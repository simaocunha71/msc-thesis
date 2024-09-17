
def is_Sub_Array(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            return True
    return False


