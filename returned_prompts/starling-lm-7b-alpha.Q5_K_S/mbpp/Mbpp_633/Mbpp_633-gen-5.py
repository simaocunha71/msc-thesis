def pair_xor_Sum(arr, x):
    total = 0
    for i in range(len(arr)):
        total += x ^ arr[i]
    return total

#Test
assert pair_xor_Sum([5,9,7,6],4) == 47

#Another approach using two pointers
def pair_xor_Sum2(arr, x):
    total = 0
    left = 0
    right = 0
    while left < len(arr):
        while right < len(arr) and x ^ arr[left] > arr[right]:
            right += 1
        total += arr[right]
        left += 1
        right += 1
    return total

#Test
assert pair_xor_Sum2([5,9,7,6],4) == 47

#Another approach using two pointers and set
def pair_xor_Sum3(arr, x):
    total = 0
    left = 0
    right = 0
    arr_set = set(arr)
    while left < len(arr):
        while right < len(arr) and x ^ arr[left] not in arr_set:
            right += 1
        total += arr[right]
        left += 1
        right += 1
    return total

#Test
assert pair_xor_Sum3([5,9,7,6],4) == 47

#Another approach using two pointers and set
def pair_xor_Sum4(arr, x):
    total = 0
    left = 0
    right = 0
    arr_set = set(arr)
    while left < len(arr):
        while right < len(arr) and (x ^ arr[left]) not in arr_set:
            right += 1
        total += arr[right]
        left += 1
        right += 1
    return total

#Test
assert pair_xor_Sum4([5,9,7,6],4) == 47

#Another approach using two pointers and set
def pair_xor_Sum5(arr, x