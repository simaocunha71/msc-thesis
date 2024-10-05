    def strange_sort_list(lst):
        result = []
        while len(lst) > 0:
            result.append(min(lst))
            lst.remove(min(lst))
            if len(lst) > 0:
                result.append(max(lst))
                lst.remove(max(lst))
        return result
    # Test cases
    print(strange_sort_list([1, 2, 3, 4]))  # [1, 4, 2, 3]
    print(strange_sort_list([5, 5, 5, 5]))  # [5, 5, 5, 5]
    print(strange_sort_list([]))  # []
    print(strange_sort_list([1, 3, 2, 4]))  # [1, 4, 2, 3]
    print(strange_sort_list([5, 3, 2, 4]))  # [2, 5, 3, 4]  # 4 is the smallest of the remaining elements
    print(strange_sort_list([1, 5, 3, 4, 2]))  # [1, 5, 2, 4, 3]  # 3 is the smallest of the remaining elements
    # Check for edge cases
    print(strange_sort_list([1]))  # [1]
    print(strange_sort_list([1, 2]))  # [1, 2]
    print(strange_sort_list([1, 2, 3]))  # [1, 3, 2]  # 2 is the smallest of the remaining elements
    print(strange_sort_list([1, 2, 3, 4, 5]))  # [1, 5, 2, 4, 3]  # 3 is the smallest of the remaining elements
    print(strange_sort_list([1, 2, 3, 4, 5, 6]))  # [1, 6, 2, 5, 3, 4]  # 4 is the smallest of the remaining elements

    # Check for empty list
    print(strange_sort_list([]))  # []
    # Check for single element list
    print(strange_sort_list([1]))  # [1]
    # Check for duplicate elements list
    print(strange_sort_list([5, 5, 5, 