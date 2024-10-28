
def find_first_occurrence(arr, num):
    if arr[0] == num:
        return 0
    for i in range(1, len(arr)):
        if arr[i] == num:
            return i
    return -1


