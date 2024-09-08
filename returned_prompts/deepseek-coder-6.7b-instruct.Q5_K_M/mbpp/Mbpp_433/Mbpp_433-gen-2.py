def check_greater(arr, num):
    for i in arr:
        if i <= num:
            return False
    return True

print(check_greater([1, 2, 3, 4, 5], 4))  # False

# Task 2
