def long_words(n,words):
    result = [word for word in words.split() if len(word) > n]
    return result

print(long_words(3,"python is a programming language"))

# Output: ['python', 'programming', 'language']

"""
Explanation:
The function long_words takes an integer n and a string words as input. The string words is split into a list of words using the split() function. Then it uses a list comprehension to create a new list, result, containing only the words in words that have more than n characters. Finally, the function returns the result.
"""
<jupyter_output>
['python', 'programming', 'language']
<jupyter_text>
