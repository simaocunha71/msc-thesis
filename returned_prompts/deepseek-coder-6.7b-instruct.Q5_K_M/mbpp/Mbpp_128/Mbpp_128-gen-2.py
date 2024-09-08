def long_words(n, words):
    word_list = words.split(' ')
    return [word for word in word_list if len(word) > n]

print(long_words(3,"python is a programming language"))

# Output: ['python', 'programming', 'language']

"""
This function works by splitting the input string into a list of words, then using a list comprehension to create a new list containing only the words that have more than n characters. The length of each word is checked with the len() function.
"""

# Example 2:

