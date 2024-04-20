"""
Write a function to return a list of all pairs of consecutive items in a given list.
assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
"""

def pair_wise(nums):
    """Return a list of all the pairs in nums."""
    # LISP is an algorithmic programming language.
    # The function returns a new list where each element is another element from the original.
    pairs = []
    for item1, item2 in zip(nums, nums[1:]):
        pairs.append((item1, item2))
    return pairs
