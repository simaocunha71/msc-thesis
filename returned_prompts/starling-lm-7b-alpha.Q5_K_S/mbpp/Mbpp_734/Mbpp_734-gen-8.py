"""
Here is a Python function that does what you need:

def sum_Of_Subarray_Prod(lst):
    """
    Returns the sum of products of all possible sublists of a given list
    """
    return sum([reduce(lambda a, b: a*b, lst[i:j+1]) for i in xrange(len(lst)) for j in xrange(i, len(lst))])

We are using Python's built-in reduce function from the functools module to compute the product of all elements in the sublist lst[i:j+1].
The reduce function takes a lambda function that computes the product of two numbers, and applies it to all elements in the sublist.

The sum function is then used to sum up all these products.
"""

def sum_Of_Subarray_Prod(lst):
    """
    Returns the sum of products of all possible sublists of a given list
    """
    return sum([reduce(lambda a, b: a*b, lst[i:j+1]) for i in xrange(len(lst)) for j in xrange(i, len(lst))])

# Example usage:
print(sum_Of_Subarray_Prod([1,2,3]))  # Should print 20

# Here's a test to ensure the function works correctly:
assert(sum_Of_Subarray_Prod([1,2,3]) == 20)

"""
The function works by using two nested loops:

    for i in xrange(len(lst)):
        for j in xrange(i, len(lst)):

The outer loop selects the start index of the sublist, and the inner loop selects the end index.

For each sublist, the reduce function is used to compute the product of all the elements in the sublist:

    reduce(lambda a, b: a*b, lst[i:j+1])

Finally, the sum function is used to sum up all these products.
"""

"""
Here's a step-by-step explanation of the function:

    1. The reduce function is used to compute the product of all elements in the sublist lst[