    # First, reverse the array
    arr.reverse()

    # Now, compare the original array to the reversed array
    # and count the number of changes needed to make the arrays the same
    count = 0
    for i in range(len(arr)):
        if arr[i] != arr[i-1]:
            count += 1

    return count
