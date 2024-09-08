def reverse_words(s):
    return ' '.join(s.split()[::-1])

print(reverse_words("python program"))

#Output: program python

"""
Explanation:
In this code, we are using the split() function to split the string into a list of words. We then use the [::-1] slice to reverse the order of the words in the list. Finally, we use the join() function to concatenate the words back into a string, with a space between each word.
"""
<jupyter_output>
program python
<jupyter_text>
**Question 2**
<jupyter_code>
