    def strange_sort_list(lst):
        result = []
        while lst:
            min_val = min(lst)
            result.append(min_val)
            lst.remove(min_val)
            if lst:
                max_val = max(lst)
                result.append(max_val)
                lst.remove(max_val)
        return result
    # Test cases
    print(strange_sort_list([1, 2, 3, 4]))  # [1, 4, 2, 3]
    print(strange_sort_list([5, 5, 5, 5]))  # [5, 5, 5, 5]
    print(strange_sort_list([]))  # []
    print(strange_sort_list([1, 2, 3, 4, 5]))  # [1, 5, 2, 4, 3]
    print(strange_sort_list([5, 2, 8, 1, 9]))  # [1, 9, 2, 8, 5]