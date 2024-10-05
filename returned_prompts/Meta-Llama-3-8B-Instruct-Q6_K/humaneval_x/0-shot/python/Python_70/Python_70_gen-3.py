    def strange_sort_list(lst):
        if not lst:
            return []
        sorted_lst = sorted(lst)
        result = []
        while sorted_lst:
            result.append(sorted_lst.pop(0))
            if sorted_lst:
                result.append(sorted_lst.pop())
        return result

    print(strange_sort_list([1, 2, 3, 4]))  # Output: [1, 4, 2, 3]
    print(strange_sort_list([5, 5, 5, 5]))  # Output: [5, 5, 5, 5]
    print(strange_sort_list([]))  # Output: []


Explanation:
This function takes a list of integers as input and returns the list in a strange order, which is defined as the minimum value, then maximum of the remaining integers, then minimum and so on. 

The function first checks if the input list is empty. If it is, it returns an empty list.

If the list is not empty, it sorts the list in ascending order using the sorted() function. Then, it initializes an empty list result to store the sorted list in the strange order.

The function then enters a loop that continues until the sorted list is empty. In each iteration of the loop, it pops the smallest element from the sorted list and adds it to the result list. If the sorted list is not empty after popping the smallest element, it pops the largest element from the sorted list and adds it to the result list.

Finally, the function returns the result list, which is the input list in the strange order. 

The function is tested with three examples: [1, 2, 3, 4], [5, 5, 5, 5], and an empty list. The output for each example is as expected. 

The time complexity of this function is O(n log n) due to the sorting operation, where n is the length of the input list. The space complexity is O(n) due to the creation of the result list and the temporary lists used during the sorting operation. 







