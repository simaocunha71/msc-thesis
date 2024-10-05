
def maximum(arr, k):
    # Sort array in ascending order
    arr.sort()
    # Return the last k elements of the array
    return arr[-k:]

# Time complexity: O(n)
# Space complexity: O(1)

# This solution is simple and efficient, with a time complexity of O(n) and space complexity of O(1).
# It first sorts the array in ascending order, which takes O(nlogn) time and O(1) space.
# Then, it returns the last k elements of the array, which takes O(n) time and O(1) space.
# Therefore, the overall time complexity is O(n), and the overall space complexity is O(1).

# However, note that this solution modifies the original array, which may not be desirable if the array is needed in its original form.
# A more flexible solution would be to create a copy of the array and return the maximum k numbers from the copied array,
# while leaving the original array unchanged.

# Here is an example implementation of a more flexible solution:

def maximum(arr, k):
    # Create a copy of the array
    arr_copy = arr[:]
    # Sort the copied array in ascending order
    arr_copy.sort()
    # Return the last k elements of the copied array
    return arr_copy[-k:]

# Time complexity: O(n)
# Space complexity: O(n)

# This solution creates a copy of the array, which takes O(n) time and O(n) space.
# Then, it sorts the copied array and returns the last k elements, which takes O(nlogn) time and O(1) space.
# Therefore, the overall time complexity is O(n), and the overall space complexity is O(n).

# This solution is more flexible than the previous one, as it does not modify the original array.
# However, it is slightly less efficient in terms of space complexity, as it requires additional space to store the copied array.

# In summary, the choice between the two solutions depends on the specific requirements of the problem.
# If modifying the original array is acceptable, the first solution is simpler and more efficient.
# If preserving the original