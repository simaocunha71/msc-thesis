def find_first_occurrence(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5))

