def maximum(arr, k):
    if k == 0:
        return []
    elif k >= len(arr):
        return sorted(arr)
    else:
        max_k = sorted(arr, reverse=True)[:k]
        return sorted(max_k)

print(maximum([-3, -4, 5], 3)) # [-4, -3, 5]
print(maximum([4, -4, 4], 2)) # [4, 4]
print(maximum([-3, 2, 1, 2, -1, -2, 1], 1)) # [2]