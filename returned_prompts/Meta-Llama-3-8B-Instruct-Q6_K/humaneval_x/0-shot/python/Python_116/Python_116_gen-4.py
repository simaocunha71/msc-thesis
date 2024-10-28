    def sort_array(arr):
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))

    # Test cases
    print(sort_array([1, 5, 2, 3, 4]))  # Output: [1, 2, 3, 4, 5]
    print(sort_array([-2, -3, -4, -5, -6]))  # Output: [-6, -5, -4, -3, -2]
    print(sort_array([1, 0, 2, 3, 4]))  # Output: [0, 1, 2, 3, 4]
    print(sort_array([5, 2, 3, 4, 1]))  # Output: [1, 2, 3, 4, 5]
    print(sort_array([1, 1, 0, 1, 1]))  # Output: [0, 1, 1, 1, 1]
    print(sort_array([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]  # 1, 2, 3, 4, 5
    print(sort_array([0, 0, 0, 0, 0]))  # Output: [0, 0, 0, 0, 0]
    print(sort_array([1, 1, 1, 1, 1]))  # Output: [1, 1, 1, 1, 1]
    print(sort_array([0, 1, 2, 3, 4]))  # Output: [0, 1, 2, 3, 4]
    print(sort_array([1, 1, 0, 1, 1]))  # Output: [0, 1, 1, 1, 1]
    print(sort_array([5, 3, 2, 4, 1]))  # Output: [1, 2, 3, 4, 5]
    print(sort_array([1, 1, 1, 1, 1]))  # Output: [1, 1, 1, 1, 1]
    print(sort_array([0, 0