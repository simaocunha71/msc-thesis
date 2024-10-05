    def strange_sort_list(lst):
        if not lst:
            return []

        lst.sort()
        result = [lst[0]]
        while lst:
            lst.pop(0)
            if lst:
                lst.sort(reverse=True)
                result.append(lst.pop(0))
            if lst:
                lst.sort()
                result.append(lst.pop(0))
        return result

    # Test cases
    print(strange_sort_list([1, 2, 3, 4]))  # [1, 4, 2, 3]
    print(strange_sort_list([5, 5, 5, 5]))  # [5, 5, 5, 5]
    print(strange_sort_list([]))  # []
    print(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # [1, 9, 2, 8, 3, 7, 4, 6, 5]
    print(strange_sort_list([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))  # [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]  # [10, 2, 9, 3, 8, 4, 7, 5, 6]
    print(strange_sort_list([-1, -2, -3, -4, -5]))  # [-5, -1, -4, -2, -3]
    print(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))  # [1, 12, 2, 11, 3, 10, 4, 9, 5, 8, 6, 7]
    print(strange_sort_list([1]))  # [1]
    print(strange_sort_list([2, 1]))  # [1, 2]
    print(strange_sort_list([1, 2, 3]))  # [1, 3, 2]
    print(strange_sort_list([1, 2, 3, 4, 5