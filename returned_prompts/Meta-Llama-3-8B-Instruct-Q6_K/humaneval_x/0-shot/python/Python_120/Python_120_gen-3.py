    # Sort the array in descending order
    arr.sort(reverse=True)
    # Return the first k elements of the sorted array
    return arr[:k]  # or return arr[:k].copy() if you want a copy of the list


# Example usage:
print(maximum([-3, -4, 5], 3))  # Output: [-4, -3, 5]
print(maximum([4, -4, 4], 2))  # Output: [4, 4]
print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))  # Output: [2]  # or [1] if you want the first 1 element in the sorted array
print(maximum([1, 2, 3, 4, 5], 5))  # Output: [5, 4, 3, 2, 1]
print(maximum([1, 2, 3, 4, 5], 0))  # Output: [] (empty list)  # or raise an exception if you want to handle this case differently
print(maximum([], 3))  # Output: [] (empty list)  # or raise an exception if you want to handle this case differently
print(maximum([1], 1))  # Output: [1]
print(maximum([1, 2], 2))  # Output: [2, 1]
print(maximum([-1, -2, -3], 2))  # Output: [-1, -2]
print(maximum([-1, -2, -3], 3))  # Output: [-1, -2, -3]
print(maximum([1, 2, 3, 4, 5], 1))  # Output: [5]
print(maximum([1, 2, 3, 4, 5], 2))  # Output: [5, 4]
print(maximum([1, 2, 3, 4, 5], 3))  # Output: [5, 4, 3]
print(maximum([1, 2, 3, 4, 5], 4))  # Output: [5, 4, 3, 2]
print(maximum([1, 2, 3, 