
def smallest_change(arr):
    # your code here
    if len(arr) == 1:
        return 0

    # palindrome array
    # [1, 2, 3, 3, 2, 1]
    # [1, 2, 2, 3, 3, 2, 1]

    # step 1: convert to list
    arr = list(arr)

    # step 2: find the center of array
    center = len(arr) // 2

    # step 3: find the smallest change
    smallest = 0
    for i in range(len(arr)):
        if arr[i] != arr[center]:
            smallest += 1
            arr[center] = arr[i]
            center += 1

    return smallest


# Test case 1:
arr = [1, 2, 3, 5, 4, 7, 9, 6]
print(smallest_change(arr))  # 4

# Test case 2:
arr = [1, 2, 3, 4, 3, 2, 2]
print(smallest_change(arr))  # 1

# Test case 3:
arr = [1, 2, 3, 2, 1]
print(smallest_change(arr))  # 0
