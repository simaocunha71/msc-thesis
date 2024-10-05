    # Here's a solution using a dictionary to keep track of
    # the values we've seen so far.
    seen = {}
    for elem in l:
        # We've seen this element before. Check if its negation
        # is in the dictionary.
        if elem in seen:
            return True
        # Otherwise, add the element to the dictionary.
        seen[elem] = True
    # We've gone through the entire list without finding a pair
    # of distinct elements that sum to zero, so return False.
    return False


# Here's a solution using two pointers, one at the front of
# the list and one at the back.
def pairs_sum_to_zero_2(l):
    left, right = 0, len(l)-1
    while left < right:
        # If the sum of the elements at the left and right pointers
        # is zero, we've found our pair.
        if l[left]+l[right] == 0:
            return True
        # If the sum is less than zero, the left pointer must move
        # forward. Otherwise, the right pointer must move forward.
        elif l[left]+l[right] < 0:
            left += 1
        else:
            right -= 1
    # We've gone through the entire list without finding a pair
    # of distinct elements that sum to zero, so return False.
    return False


# Here's a solution using two nested loops. This solution is
# less efficient than the previous two, with a time complexity of
# O(n^2). However, it's much simpler to understand, and it's a
# good demonstration of how to use the `break` statement to exit a
# loop early.
def pairs_sum_to_zero_3(l):
    for left in l:
        for right in l:
            if left != right and left + right == 0:
                return True
    return False




# Code to test ____:

if __name__ == "__main__":
    print(pairs_sum_to_zero([1, 3, 5, 0]))
    print(