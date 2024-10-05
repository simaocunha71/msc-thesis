    def add(lst):
        return sum(x for i, x in enumerate(lst) if i % 2 != 0 and x % 2 == 0)
    print(add([4, 2, 6, 7]))  # Output: 2
    print(add([1, 3, 5, 6]))  # Output: 6
    print(add([10, 20, 30, 40]))  # Output: 40
    print(add([1, 2, 3, 4]))  # Output: 4
    print(add([5, 6, 7, 8]))  # Output: 6
    print(add([1, 1, 1, 1]))  # Output: 0
    print(add([2, 2, 2, 2]))  # Output: 4
    print(add([2, 4, 6, 8]))  # Output: 10
    print(add([3, 3, 3, 3]))  # Output: 0

    # Test cases
    print(add([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))  # Output: 8
    print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: 20
    print(add([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))  # Output: 0
    print(add([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))  # Output: 20
    print(add([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))  # Output: 0
    print(add([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))  # Output: 60
    print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11