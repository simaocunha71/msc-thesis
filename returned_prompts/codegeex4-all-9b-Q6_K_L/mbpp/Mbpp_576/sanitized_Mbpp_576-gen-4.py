def is_Sub_Array(arr1, arr2):
    try:
        return arr2.index(arr1[0]) >= 0
    except ValueError:
        return False