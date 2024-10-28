# Here's a possible solution:
def sort_array(array):
    # If the length of the array is 0 or 1, there's nothing to sort.
    if len(array) <= 1:
        return array
    # We'll split the array in half and recursively sort each half.
    left, right = array[:len(array) // 2], array[len(array) // 2:]
    # Sorting the left and right halves.
    left.sort()
    right.sort(reverse=True)
    # If the sum of the first and last elements of the array is even, we'll sort in ascending order.
    # Otherwise, we'll sort in descending order.
    if sum(array[0], array[-1]) % 2 == 0:
        return left + right
    return right + left

# Testing the function:
print(sort_array([])) # => []
print(sort_array([5])) # => [5]
print(sort_array([2, 4, 3, 0, 1, 5])) # => [0, 1, 2, 3, 4, 5]
print(sort_array([2, 4, 3, 0, 1, 5, 6])) # => [6, 5, 4, 3, 2, 1, 0]

# Here's a possible solution:
def sort_array(array):
    # If the length of the array is 0 or 1, there's nothing to sort.
    if len(array) <= 1:
        return array
    # We'll split the array in half and recursively sort each half.
    left, right = array[:len(array) // 2], array[len(array) // 2:]
    # Sorting the left and right halves.
    left.sort()
    right.sort(reverse=True)
    # If the sum of the first and last elements of the array is even, we'll sort in ascending order.
    # Otherwise, we'll sort in descending order.
    if sum(array[0], array[-1]) % 