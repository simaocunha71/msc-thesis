"""
def max_Abs_Diff(arr):
    max_diff = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if abs(arr[i]-arr[j]) > max_diff:
                max_diff = abs(arr[i]-arr[j])
    return max_diff
"""

def max_Abs_Diff(arr):
    arr.sort()
    return arr[-1] - arr[0]

assert max_Abs_Diff((2,1,5,3)) == 4

# Time Complexity: O(n log(n))
# Space Complexity: O(1)
# This solution uses the sort method to sort the array in ascending order,
# then returns the difference between the last and first elements.
# The time complexity is O(n log(n)) due to the sort method.
# The space complexity is O(1) as the only additional memory used is the
# max_diff variable to store the maximum difference found so far.


# Here's a better solution that uses the max and min functions to find the
# maximum and minimum elements in the array, then returns the difference between them.
# This solution has a time complexity of O(n) and a space complexity of O(1).

def max_Abs_Diff(arr):
    return max(arr) - min(arr)

assert max_Abs_Diff((2,1,5,3)) == 4

# Time Complexity: O(n)
# Space Complexity: O(1)

# Here's another solution that uses the built-in max and min functions to find the
# maximum and minimum elements in the array, then returns the difference between them.
# This solution has a time complexity of O(n) and a space complexity of O(1).

def max_Abs_Diff(arr):
    return max(arr) - min(arr)

assert max_Abs_Diff((2,1,5,3)) == 4

# Time Complexity: O(n)
# Space Complexity: O(1)

# Here's another solution that uses a while loop to iterate over the array and