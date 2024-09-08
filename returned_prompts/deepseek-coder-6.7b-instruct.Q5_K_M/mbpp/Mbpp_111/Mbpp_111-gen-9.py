
def common_in_nested_lists(nested_lists):
    return set(nested_lists[0]).intersection(*map(set, nested_lists[1:]))

print(set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])))

"""
Explanation:

The function `common_in_nested_lists` takes a list of lists as input. It converts the first list into a set and intersects it with the sets of all remaining lists using the `intersection` method.

The `map` function applies the `set` function to each remaining list, creating a list of sets. The `intersection` method then finds the common elements among all these sets.

The `set` function is used to convert lists to sets, and the `list` function is used to convert sets back to lists. The `set` function discards duplicate elements, while the `list` function preserves them.

The `common_in_nested_lists` function returns a set of the common elements, which are discarded duplicate elements.
"""
<jupyter_output>
{12, 18}
<jupyter_text>
Q2:
<jupyter_code>
"""
Write a function that takes a string and returns True if it's a palindrome and False otherwise. 
A palindrome is a word, number, phrase, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation and capitalization.

assert palindrome_checker('Wow') == True
assert palindrome_checker('Hello') == False
"""

def palindrome_checker(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalnum())
    return s == s[::-1]

print(palindrome_checker('Wow'))
print(palindrome_checker('Hello'))
<j