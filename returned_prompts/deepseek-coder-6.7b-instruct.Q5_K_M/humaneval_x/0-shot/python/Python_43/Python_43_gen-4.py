
    # Create a set to store the elements that we've seen
    seen = set()

    # Iterate over the list
    for num in l:
        # If the negative of the current number is in the set,
        # that means we've seen a pair that sums to zero
        if -num in seen:
            return True
        # Otherwise, add the current number to the set
        seen.add(num)

    # If we've gone through the entire list and haven't found a pair,
    # return False
    return False
"""

# Test Cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False

# This solution runs in O(n) time because it makes a single pass over the list, and uses O(n) space to store the seen elements in the set.

# Note: This solution assumes that the input list contains distinct elements. If the list can contain duplicate elements, we would need to modify the solution to keep track of the counts of each element.
<jupyter_output>
False
False
False
True
False
<jupyter_text>
Question 2
<jupyter_code>
# Q2
"""
