
    lst.sort()
    result = []
    while lst:
        result.append(lst.pop(0))
        if lst:
            result.append(lst.pop())
    return result

print(strange_sort_list([1, 2, 3, 4]))
print(strange_sort_list([5, 5, 5, 5]))
print(strange_sort_list([]))

This Python program takes a list of integers as input, sorts it in ascending order, and then iteratively takes the smallest and largest remaining elements, appending them to a new list until all elements have been used. The function then returns this new list.
<jupyter_output>
<empty_output>
<jupyter_text>
2. Write a Python function, `merge_sorted_lists(lst1, lst2)`, that takes two sorted lists of integers as input and returns a single sorted list containing all of the elements from both input lists. For example, `merge_sorted_lists([1, 3, 5], [2, 4, 6])` should return `[1, 2, 3, 4, 5, 6]`. Note: This function should not use the built-in sort function or similar. Instead, it should use the merge process of the merge sort algorithm, which works by comparing the elements of the two lists and taking the smaller of the two elements at a time.
<jupyter_code>
