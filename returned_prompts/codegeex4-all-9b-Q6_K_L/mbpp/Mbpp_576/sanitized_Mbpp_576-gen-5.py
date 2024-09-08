def is_Sub_Array(arr1, arr2):
    """
    Check if arr1 is a sublist of arr2
    """
    return any(arr1[i:i+len(arr1)] == arr1 for i in range(len(arr2)-len(arr1)+1))