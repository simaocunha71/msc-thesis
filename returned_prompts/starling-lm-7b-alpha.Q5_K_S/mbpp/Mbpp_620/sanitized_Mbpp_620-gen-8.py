from collections import deque
def largest_subset(lst):
    """
    Find the size of the largest subset of a list of numbers so that every pair is divisible.

    >>> largest_subset([1, 3, 6, 13, 17, 18])
    4
    """
    lst.sort()
    stack = []
    for i, e in enumerate(lst):
        if stack and stack[-1] % 2 == e % 2:
            stack.pop()
        else:
            stack.append(e)
    return len(stack)