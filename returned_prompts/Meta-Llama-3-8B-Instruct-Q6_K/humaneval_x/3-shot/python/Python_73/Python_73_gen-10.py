    arr = list(map(str, arr))  # convert to strings for easy reversal
    arr = ''.join(arr)  # join the strings into one
    arr = arr[::-1]  # reverse the string
    arr = list(map(int, arr))  # convert back to integers
    diff = 0
    for i in range(len(arr)):
        if arr[i] != arr[-i - 1]:
            diff += 1
    return diff


