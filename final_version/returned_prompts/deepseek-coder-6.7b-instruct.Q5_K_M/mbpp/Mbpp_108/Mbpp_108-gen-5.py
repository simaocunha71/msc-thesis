def merge_sorted_list(list1, list2, list3):
    return sorted(list1+list2+list3)

print(merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48]))

"""
This function merges the three input lists into a single list using the '+' operator, then sorts that list using Python's built-in 'sorted' function.
"""

"""
This function works by merging the three lists into a single list using the '+' operator, then sorts the resulting list in ascending order using Python's built-in 'sorted' function.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
2. Write a Python function to check whether a given string is a pangram or not. A pangram is a sentence containing every letter of the alphabet at least once. For example : "The quick brown fox jumps over the lazy dog"
<jupyter_code>
