def check_greater(arr, n):
    return all(i > n for i in arr)

print(check_greater([1, 2, 3, 4, 5], 4))  # False

