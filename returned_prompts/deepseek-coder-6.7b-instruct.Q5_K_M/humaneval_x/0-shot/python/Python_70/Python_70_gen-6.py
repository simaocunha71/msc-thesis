
    def strange_sort_list(lst):
        lst.sort()
        output = []
        while len(lst) > 0:
            output.append(lst.pop(0))
            if len(lst) > 0:
                output.append(lst.pop())
        return output

    print(strange_sort_list([1, 2, 3, 4]))  # [1, 4, 2, 3]
    print(strange_sort_list([5, 5, 5, 5]))  # [5, 5, 5, 5]
    print(strange_sort_list([]))  # []

Explanation:

This solution works by first sorting the input list in ascending order. Then it constructs the output list by alternating between popping the smallest and largest remaining elements from the input list.

The while loop continues until the input list is empty. For each iteration of the loop, the smallest and largest remaining elements are appended to the output list in this order.

If the input list is empty at the start of the loop, the function returns an empty list immediately.

The time complexity of this solution is O(n log n) due to the sorting operation, and the space complexity is O(n) for the output list.

This solution assumes that all input lists will have integers. If this assumption is not valid, additional error checking should be added to the function.

This solution is also not optimized for large inputs. For large inputs, a more efficient algorithm would be needed. However, this solution should work fine for small to medium-sized inputs.
    '''

# 3.1.10
# 