
def interleave_lists(a, b, c):
    return [val for pair in zip(a, b, c) for val in pair]

print(interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]))

"""
Explanation:

The function interleave_lists takes three lists as arguments. It uses the built-in zip function to pair up the elements from the three lists in the same order. The zip function returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The resulting iterator is used by the list comprehension to generate a single flat list of the elements from the three input lists in an interleaved manner.

The resulting list is returned by the function.

This solution works by zipping the three input lists together, which pairs up the corresponding elements from the three lists. The list comprehension then flattens this out into a single list by iterating over the pairs and the elements within the pairs.
"""
<jupyter_output>
[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
<jupyter_text>
2. Write a Python function to check whether a string is a pangram or not. A pangram is a sentence containing every letter of the alphabet at least once. The most famous English pangram is: "The quick brown fox jumps over the lazy dog".
<jupyter_code>
