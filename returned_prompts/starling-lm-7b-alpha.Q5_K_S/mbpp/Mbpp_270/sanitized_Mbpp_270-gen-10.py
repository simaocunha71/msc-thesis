def sum_even_and_even_index(arr):
    result = 0
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] % 2 == 0:
            result += arr[i]
    return result