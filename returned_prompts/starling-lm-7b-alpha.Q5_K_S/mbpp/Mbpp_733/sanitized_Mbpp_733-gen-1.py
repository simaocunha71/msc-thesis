def find_first_occurrence(arr, x):
    if x not in arr:
        return -1
    else:
        for i in range(len(arr)):
            if arr[i]==x:
                return i