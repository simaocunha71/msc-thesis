
def is_Sub_Array(arr1, arr2) :
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                break
        else:
            continue
        for k in range(i, len(arr1)):
            if arr1[k] != arr2[j]:
                break
        else:
            return True
    return False


