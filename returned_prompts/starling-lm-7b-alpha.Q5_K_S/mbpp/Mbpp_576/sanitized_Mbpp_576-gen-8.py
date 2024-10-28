def is_Sub_Array(arr1, arr2):
    if len(arr2) > len(arr1):
        return False
    for i in range(len(arr1)-len(arr2)+1):
        if arr2 == arr1[i:i+len(arr2)]:
            return True
    return False
arr1 = [1,4,3,5]
arr2 = [1,2]