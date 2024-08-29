"""
This problem can be solved using python's built-in zip function to iterate through the two lists simultaneously. If the elements in the same index are the same, then increment the counter.
"""

def count_same_pair(list1, list2):
    return sum(1 for a, b in zip(list1, list2) if a == b)

print(count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])) # Output: 4


"""
The sum() function returns the sum of the elements in the list. The expression in the parentheses for the sum() function is a generator expression that iterates through the elements in the list (a, b) in the same order as the zip() function. If the elements are the same (a == b), then it returns 1; if they're not, it returns 0. So, effectively, the sum() function counts the number of elements that are the same in the two lists.
"""


"""
This solution has a time complexity of O(n), where n is the length of the input lists. This is because the zip() and sum() functions iterate through the input lists once each. The space complexity is O(1), which means that the space used does not grow with the size of the input.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2
<jupyter_code>
