def is_Sub_Array(arr1, arr2):
    if len(arr1) > len(arr2):
        return False
    for i in range(len(arr2)-len(arr1)+1):
        if arr1 == arr2[i:i+len(arr1)]:
            return True
    return False