def long_words(n, words):
    return [word for word in words.split() if len(word) > n]

print(long_words(3, "python is a programming language"))

"""
Explanation:
In this code, we're defining a function long_words that takes two arguments: n, which is the minimum length of words we're interested in, and words, which is the string of words we're analyzing.

Inside the function, we use a list comprehension to create a new list of words that are longer than n characters. We do this by splitting the words string into a list of words using the split method, and then iterating over that list with a for loop. For each word, we add it to the new list if its length is greater than n.

Finally, we return the new list.

When we call long_words(3, "python is a programming language"), we get ['python', 'programming', 'language'], which are the words in the string "python is a programming language" that are longer than 3 characters.
"""
<jupyter_output>
['python', 'programming', 'language']
<jupyter_text>
Question 4
<jupyter_code>
