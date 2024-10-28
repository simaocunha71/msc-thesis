    def strange_sort_list(lst):
        if not lst:
            return []
        lst.sort()
        result = []
        while lst:
            result.append(lst.pop(0))
            if lst:
                result.append(max(lst))
                lst.remove(max(lst))
        return result
    # Test cases
    print(strange_sort_list([1, 2, 3, 4]))  # Expected output: [1, 4, 2, 3]
    print(strange_sort_list([5, 5, 5, 5]))  # Expected output: [5, 5, 5, 5]
    print(strange_sort_list([]))  # Expected output: []


Explanation:
The function `strange_sort_list` takes a list of integers as input and returns a list in a strange order. The strange sorting is done by starting with the minimum value, then maximum of the remaining integers, then minimum and so on.

Here is the implementation:

1. First, we check if the input list is empty. If it is, we return an empty list.

2. Next, we sort the list in ascending order.

3. Then, we create an empty list `result` to store the sorted list.

4. We loop until the input list is empty.

5. In each iteration, we pop the first element from the input list and append it to the `result` list.

6. If the input list is not empty after popping the first element, we find the maximum value in the remaining elements, remove it from the list, and append it to the `result` list.

7. Finally, we return the `result` list.

The test cases at the end of the code verify that the function works correctly for different inputs. For example, `strange_sort_list([1, 2, 3, 4])` returns `[1, 4, 2, 3]`, which is the expected output for this input. Similarly, `strange_sort_list([5, 5, 5, 5])` returns `[5, 5, 5, 5]`, and `strange_sort_list([])` returns an empty list.