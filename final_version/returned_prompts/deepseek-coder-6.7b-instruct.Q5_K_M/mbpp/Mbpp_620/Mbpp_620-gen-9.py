"""
The problem can be solved by dynamic programming. 

We can start by sorting the array and then we can iterate through the array to find the longest subset of divisible numbers.

We will use a list to store the longest subset ending at each position.

In the end, we will return the maximum value from the list.
"""

def largest_subset(lst):
    # sort the list
    lst.sort()
    # initialize the list of sizes
    sizes = [1]*len(lst)
    # iterate through the list
    for i in range(len(lst)):
        for j in range(i):
            # if the pair is divisible
            if lst[i] % lst[j] == 0:
                # update the size of the largest subset
                sizes[i] = max(sizes[i], sizes[j] + 1)
    # return the maximum size
    return max(sizes)

# test the function
assert largest_subset([1, 3, 6, 13, 17, 18]) == 4

"""
This function works by iterating through the list and for each number, it checks all the previous numbers to see if they can divide it. 

If they can, it updates the size of the largest subset at the current position. 

Finally, it returns the maximum size of the subset found.
"""

# test the function with other examples
assert largest_subset([1, 2, 4, 8, 16]) == 5
assert largest_subset([3, 9, 27, 81, 243]) == 5
assert largest_subset([2, 4, 8, 16, 32]) == 6
assert largest_subset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
assert largest_subset([10, 20, 30, 40, 50]) == 2
assert largest_subset([1, 2, 4, 8, 16, 32, 64]) == 5
assert largest_subset([3, 