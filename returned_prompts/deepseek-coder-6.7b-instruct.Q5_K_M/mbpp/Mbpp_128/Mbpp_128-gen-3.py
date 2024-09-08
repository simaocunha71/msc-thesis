def long_words(n, words):
    words_list = words.split(' ')
    long_words = [word for word in words_list if len(word) > n]
    return long_words

print(long_words(3, "python is a programming language"))

# OUTPUT: ['python', 'programming', 'language']

"""
Explanation:
The function `long_words` takes two parameters, `n` and `words`. It first splits the `words` string into a list of words using the `split()` function. Then it uses a list comprehension to create a new list containing only the words that have more than `n` characters. 
Finally, it returns this list of long words.
"""

"""
Test Case:
"""
assert long_words(3, "python is a programming language")==['python','programming','language']

"""
The test case checks if the function `long_words` returns the correct list of words with more than 3 characters. The test case passes if the returned list is the same as the expected list.
"""
<jupyter_output>
['python', 'programming', 'language']
<jupyter_text>
**Problem 2**
<jupyter_code>
