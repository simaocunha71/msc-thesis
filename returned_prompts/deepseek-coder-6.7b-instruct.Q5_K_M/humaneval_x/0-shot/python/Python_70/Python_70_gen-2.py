
    lst.sort()
    result = []
    while lst:
        result.append(lst.pop(0))
        if lst:
            result.append(lst.pop())
    return result

print(strange_sort_list([1, 2, 3, 4]))  # [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5]))  # [5, 5, 5, 5]
print(strange_sort_list([]))  # []

This program works by sorting the input list in ascending order, then it alternates between popping the smallest and largest remaining elements from the list, appending them to the result, and repeating until the list is empty.
</code>

## Code Explanation

1. The function takes a list of integers as an argument.

2. The list is sorted in ascending order using the sort() function.

3. A new empty list is initialized to store the sorted elements in the required strange order.

4. The function then enters a loop that continues until the list is empty.

5. Inside the loop, the smallest element from the list is popped and appended to the result list using the pop(0) method.

6. If there are still elements in the list, the largest element is popped from the end of the list using the pop() method.

7. This process is repeated until all elements in the original list have been added to the result list in the required order.

8. Finally, the function returns the result list.

This solution has a time complexity of O(n log n) due to the sorting operation, where n is the number of elements in the input list.
</code>

## Code Explanation

1. The function takes a list of integers as an argument.

2. The list is sorted in ascending order using the sort() function.

3. A new empty list is initialized to store the sorted elements in the required strange order.

4. The function then enters a loop that continues until the list is empty.

5. Inside the loop, the smallest element from the list is popped and appended to