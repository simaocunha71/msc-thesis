def strange_sort_list(lst):
    if len(lst) == 0:
        return []
    else:
        lst.sort()
        result = []
        left = 0
        right = len(lst) - 1

        while left <= right:
            result.append(lst[left])
            if left != right:
                result.append(lst[right])
            left += 1
            right -= 1

        return result

print(strange_sort_list([1, 2, 3, 4])) # [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5])) # [5, 5, 5, 5]
print(strange_sort_list([])) # []
print(strange_sort_list([7, 7, 7, 7])) # [7, 7, 7, 7]
print(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]