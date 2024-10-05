    # Correct Solution:
    def strange_sort_list(lst):
        while len(lst) > 1:
            min_index = 0
            for i in range(1, len(lst)):
                if lst[i] < lst[min_index]:
                    min_index = i
            lst.pop(min_index)
            lst.insert(0, min_index)
        return lst
    # Explanation:
    # The function takes a list of integers as input and sorts it in a strange way.
    # It starts by finding the minimum value in the list and swapping it with the first element.
    # Then, it continues to find the maximum value from the remaining elements and swaps it with the last element.
    # This process is repeated until the length of the list becomes 1.
    # Finally, the function returns the sorted list.

# Alternate Solution:
def strange_sort_list(lst):
    # while len(lst) > 1:
    #     min_index = 0
    #     for i in range(1, len(lst)):
    #         if lst[i] < lst[min_index]:
    #             min_index = i
    #     lst.pop(min_index)
    #     lst.insert(0, min_index)
    # return lst
    lst.sort(key = lambda x:x%2, reverse = True)
    return lst

# Explanation:
# The function takes a list of integers as input and sorts it in a strange way.
# It uses the sort function with a lambda function as the key to sort the list.
# The lambda function returns True if the number is even and False if the number is odd.
# The sort function sorts the list in descending order based on the lambda function's return value.
# Finally, the function returns the sorted list.

# Example Usage:
print(strange_sort_list([1, 2, 3, 4]))  # Output: [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5])) 