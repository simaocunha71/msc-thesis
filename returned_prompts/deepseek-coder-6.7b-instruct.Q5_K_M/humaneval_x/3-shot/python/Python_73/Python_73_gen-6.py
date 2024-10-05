    i = 0
    j = len(arr) - 1
    changes = 0

    while i < j:
        if arr[i] != arr[j]:
            changes += 1
        i += 1
        j -= 1

    return changes

The main idea is to compare the elements from the start and the end of the array, if they are not equal, we increment our counter.

