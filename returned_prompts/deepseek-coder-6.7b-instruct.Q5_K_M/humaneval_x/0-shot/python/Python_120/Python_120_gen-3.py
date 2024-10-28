
    def maximum(arr, k):
        arr.sort()
        return arr[-k:]

    arr = [-3, -4, 5]
    k = 3
    print(maximum(arr, k))  # Output: [-4, -3, 5]

    arr = [4, -4, 4]
    k = 2
    print(maximum(arr, k))  # Output: [4, 4]

    arr = [-3, 2, 1, 2, -1, -2, 1]
    k = 1
    print(maximum(arr, k))  # Output: [2]

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 5
    print(maximum(arr, k))  # Output: [6, 7, 8, 9, 10]

    arr = [-1000, -999, -998, -997, -996, -995, -994, -993, -992, -991]
    k = 5
    print(maximum(arr, k))  # Output: [-991, -992, -993, -994, -995]

    arr = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]
    k = 5
    print(maximum(arr, k))  # Output: [991, 992, 993, 994, 995]

    arr = [-3, -2, -1, 1, 2, 3]
    k = 3
    print(maximum(arr, k))  # Output: [-1, -2, -3]

    arr = [1, 1, 1, 1, 1, 1, 1]
    k = 3
