    arr.sort()
    start_index = len(arr) // 2
    if len(arr) % 2 == 0:
        end_index = start_index - 1
    else:
        end_index = start_index

    odd_count = 0
    for i in range(start_index, end_index + 1):
        if arr[i] != arr[start_index]:
            odd_count += 1

    return odd_count


