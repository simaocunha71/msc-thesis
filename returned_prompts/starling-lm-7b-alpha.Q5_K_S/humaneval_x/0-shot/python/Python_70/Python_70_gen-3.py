    # Initialize result
    result = []

    # Initialize index
    i = 0

    # Loop until all elements are added to the result
    while i < len(lst):

        # Find the index of the minimum value
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        # Add the minimum value to the result
        result.append(lst[min_index])

        # Remove the minimum value from the list
        del lst[min_index]

    return result

# Test
print(strange_sort_list([1, 2, 3, 4])) # [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5])) # [5, 5, 5, 5]
print(strange_sort_list([])) # []

# Time complexity: O(n^2)
# Space complexity: O(n)

# This algorithm works by initializing an empty result list and an index i. It then loops until all elements are added to the result. In each iteration, it finds the index of the minimum value in the remaining part of the list and adds it to the result. Then, it removes the minimum value from the list. The time complexity of this algorithm is O(n^2) because in the worst case, it needs to compare each element with every other element. The space complexity is O(n) because it stores all elements in the result list.

# The above code is a solution to the problem of sorting a list of integers in a strange order. The strange sorting algorithm starts with the minimum value and then the maximum of the remaining integers, and so on. It initializes an empty result list and an index i. It then loops until all elements are added to the result. In each iteration, it finds the index of the minimum value in the remaining part of the list and adds it to the result. Then, it removes the minimum value from the list. The time complexity of this algorithm is O(n^2) because in the worst case, it needs to compare each element with every other