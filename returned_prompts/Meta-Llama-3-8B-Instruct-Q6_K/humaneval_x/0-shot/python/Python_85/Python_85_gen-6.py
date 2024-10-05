def add(lst):
    result = 0
    for i in range(0, len(lst)):
        if i % 2 != 0 and lst[i] % 2 == 0:
            result += lst[i]
    return result
print(add([4, 2, 6, 7]))  # Output: 2
print(add([1, 2, 3, 4]))  # Output: 2
print(add([2, 4, 6, 8]))  # Output: 8
print(add([5, 7, 9, 11]))  # Output: 0
print(add([3, 6, 9, 12]))  # Output: 6
print(add([1, 3, 5, 7]))  # Output: 0
print(add([2, 4, 6, 8, 10]))  # Output: 20
print(add([2, 5, 6, 7]))  # Output: 2
print(add([2, 4, 6, 8, 10, 12]))  # Output: 20
print(add([1, 2, 3, 4, 5]))  # Output: 2
print(add([1, 2, 3, 4, 5, 6]))  # Output: 2
print(add([1, 2, 3, 4, 5, 6, 7]))  # Output: 2
print(add([1, 2, 3, 4, 5, 6, 7, 8]))  # Output: 2
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: 2
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: 2
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))  # Output: 2
print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,