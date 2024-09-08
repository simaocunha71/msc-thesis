def interleave_lists(l1,l2,l3):
    return [val for pair in zip(l1,l2,l3) for val in pair]

print(interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]))

"""
Explanation:
This problem can be solved by using Python's built-in `zip` function which can take multiple iterables and returns an iterator that produces tuples of the corresponding elements from each iterable.

In the problem, three lists are given. We use `zip` to pair these lists together. The result is a list of tuples where the first element is from the first list, the second is from the second list and the third is from the third list.

Then we use a list comprehension to flatten this into a single list. The outer list comprehension iterates over the pairs, and the inner list comprehension iterates over the values in each pair.

Finally, we return the result.
"""

"""
