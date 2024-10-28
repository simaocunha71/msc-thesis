from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'b'))
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'c'))
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ar'))
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], ''))
print(filter_by_prefix([], 'a'))
<jupyter_output>
['abc', 'array']
['bcd']
['cde']
['array']
['abc', 'bcd', 'cde', 'array']
[]
<jupyter_text>
Problem 2Write a function, ```common_elements```, which takes as input two lists of integers and returns a sorted list of all common elements in the two lists. For example, if the input lists are [1, 2, 3, 4] and [3, 4, 5, 6], the function should return [3, 4] as these are the elements that are common to both lists.
<jupyter_code>
