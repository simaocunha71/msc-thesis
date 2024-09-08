def reverse_Array_Upto_K(arr, k):
    for i in range(k//2):
        arr[i], arr[k-i-1] = arr[k-i-1], arr[i]
    return arr

print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4))

# Solution 2
