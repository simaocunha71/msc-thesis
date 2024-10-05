    # If list length is less than 2, return True
    if len(lst) < 2:
        return True
    # If first two elements are not in ascending order, return False
    elif lst[1] - lst[0] < 0:
        return False
    # Otherwise, recursively check the rest of the list
    else:
        return is_sorted(lst[1:])

# Time complexity analysis:
# The time complexity of this function is O(n), where n is the length of the input list.
# This is because for each element in the list, we only perform a single operation (comparing the current element with the next element).

# Space complexity analysis:
# The space complexity of this function is O(n), where n is the length of the input list.
# This is because at any point in time, we are only storing the current list and the next element of the list to compare, which takes up O(n) space.



# Here's how the function works:

# First, we check if the length of the list is less than 2. If it is, we return True, because a list with 0 or 1 element is considered sorted.

# Next, we check if the first two elements of the list are in ascending order. If they're not (i.e., the second element is less than the first), we return False, because the list is not sorted.

# If the first two elements are in ascending order, we recursively call the function with the rest of the list (everything except the first element). This allows us to check the rest of the list for sortedness.

# We continue this process until we reach the end of the list. If at any point we find that the list is not sorted, we return False. If we reach the end of the list without finding any unsorted elements, we return True.

# This recursive approach allows us to check the sortedness of the list in a single pass through the list, making it efficient.

# In terms of time complexity, the function runs in O(n) time, because for each element in the list, we perform a single operation (comparing the current element with the next element). The space complexity is also O(n), because at