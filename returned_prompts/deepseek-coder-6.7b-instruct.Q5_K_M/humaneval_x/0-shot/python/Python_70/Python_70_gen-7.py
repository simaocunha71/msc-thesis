
    lst.sort()
    result = []

    while lst:
        result.append(lst.pop(0))
        if lst:
            result.append(lst.pop())

    return result

# Test cases
print(strange_sort_list([1, 2, 3, 4])) #  [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5])) #  [5, 5, 5, 5]
print(strange_sort_list([])) #  []

# This is a simple and efficient solution to the problem. It sorts the list, then pops the minimum and maximum values from the list and appends them to the result list, until the list is empty. The time complexity is O(n log n) due to the sorting operation, and the space complexity is O(n) for the result list.
<jupyter_output>
[1, 4, 2, 3]
[5, 5, 5, 5]
[]
<jupyter_text>
