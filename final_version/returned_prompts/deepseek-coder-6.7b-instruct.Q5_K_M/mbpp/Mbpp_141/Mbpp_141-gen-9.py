def pancake_sort(lst):
    n = len(lst)
    for i in range(n):
        max_idx = max(0, lst[n-i-1:])
        if max_idx != n-i-1:
            lst[max_idx], lst[n-i-1] = lst[n-i-1], lst[max_idx]
            lst[:n-i] = lst[n-i-1:0:-1] + lst[:n-i-1]
    return lst

print(pancake_sort([15, 79, 25, 38, 69]))

# Test Cases
print(pancake_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])
print(pancake_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5])
print(pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79])
print(pancake_sort([97, 76, 45, 23, 1]) == [1, 23, 45, 76, 97])
print(pancake_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(pancake_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Note: This code will not work as expected if there are multiple instances of the same value in the list.
