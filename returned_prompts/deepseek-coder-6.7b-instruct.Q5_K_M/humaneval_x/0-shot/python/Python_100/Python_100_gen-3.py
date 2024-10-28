
    def make_a_pile(n):
        pile = []
        for i in range(n):
            if n % 2 == 0:
                pile.append(n + 2*i)
            else:
                pile.append(n + 2*i)
        return pile

    print(make_a_pile(3))


Output:

    [3, 5, 7]



The function works by initializing an empty list `pile`. Then it enters a loop that runs `n` times. In each iteration of the loop, it appends to `pile` a new element that is `n` plus `2*i`. If `n` is even, `2*i` will always be an even number, so the number of stones in the next level will be an odd number. If `n` is odd, `2*i` will be an odd number, so the number of stones in the next level will be an even number. Finally, it returns `pile`.

This function matches the description given in the question.
"""


# Test cases

# Test case 1
assert make_a_pile(3) == [3, 5, 7], "Test case 1 failed"

# Test case 2
assert make_a_pile(4) == [4, 6, 8, 10], "Test case 2 failed"

# Test case 3
assert make_a_pile(5) == [5, 7, 9, 11, 13], "Test case 3 failed"

print("All test cases passed")

"""
Output:
All test cases passed
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2Given a list of integers, return the number of pairs of integers that have the same value.
<jupyter_code>
def count_pairs(lst):
    """
    Given a list of integers, return the number of pairs of integers that have the same value.

    Examples:
    >>> count_pairs([1, 2, 3, 2, 1])
