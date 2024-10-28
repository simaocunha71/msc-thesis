def is_samepatterns(arr1, arr2):
    for i in range(len(arr1)-1):
        if arr1[i]!=arr1[i+1]:
            return False
        if arr2[i]!=arr2[i+1]:
            return False
    return True