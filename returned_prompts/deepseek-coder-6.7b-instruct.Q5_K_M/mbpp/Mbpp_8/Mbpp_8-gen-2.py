def sort_by_length(words):
    return sorted(words, key=len)

print(sort_by_length(["cat", "Always", "good", "greediness"]))

#Output: ['good', 'cat', 'Always', 'greediness']

"""
Explanation:
The function 'sort_by_length' takes a list of words as input. It uses the built-in 'sorted' function to sort the words in ascending order of their lengths. 
The 'key' argument of the 'sorted' function is set to 'len', which means that the words are sorted based on their lengths. The 'sorted' function maintains the original order of equal elements (i.e., words with the same length).
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 3: Write a Python function that takes a list of numbers and returns the sum of all the numbers in the list