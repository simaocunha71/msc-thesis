def smallest_change(arr):
    i, j = 0, len(arr) - 1
    changes = 0
    while i < j:
        if arr[i] != arr[j]:
            changes += 1
            if arr[i] < arr[j]:
                arr[j] = arr[i]
            else:
                arr[i] = arr[j]
        i += 1
        j -= 1
    return changes

print(smallest_change([1,2,3,5,4,7,9,6]))  # 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))  # 1
print(smallest_change([1, 2, 3, 2, 1]))  # 0