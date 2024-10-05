
    lst.sort()
    result = []
    while lst:
        result.append(lst.pop(0))
        if lst:
            result.append(lst.pop(-1))
    return result


print(strange_sort_list([1, 2, 3, 4]))  # [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5]))  # [5, 5, 5, 5]
print(strange_sort_list([]))  # []


# Time complexity: O(n log n) due to the sorting operation.
# Space complexity: O(n) because we are storing the result in a new list.
</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





</code>





