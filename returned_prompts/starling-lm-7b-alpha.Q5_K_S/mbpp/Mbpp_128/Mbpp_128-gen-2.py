def long_words(n,words):
    return [word for word in words.split() if len(word)>n]

long_words(3,"python is a programming language")

# Output:
['python', 'programming', 'language']



















"""
Explanation:
Here, we are using List Comprehension to make the function more readable and efficient.
The function long_words takes two arguments: n and words.
Here, n is the number of characters beyond which a word should be longer to be considered.
And words is the given list of words from which we have to find out the longer words.
In the list comprehension, we are iterating over each word in the given list of words and checking if the length of the word is greater than n.
If the length of the word is greater than n, we include that word in the result list using the [ ] brackets.
Finally, we return the result list containing all the longer words from the given list of words.
In the given assert statement, we are testing the function long_words with the inputs 3 and "python is a programming language".
As per the requirement, we should get the output ['python', 'programming', 'language'] which are the words longer than 3 characters from the given string.
"""

























"""
Explanation:
Here, we are using List Comprehension to make the function more readable and efficient.
The function long_words takes two arguments: n and words.
Here, n is the number of characters beyond which a word should be longer to be considered.
And words is the given list of words from which we have to find out the longer words.
In the list comprehension, we are iterating over each word in the given list of words and checking if the length of the word is greater than n.
If the length of the word is greater than n, we include that word in the result list using the [ ] brackets.
Finally, we return the result list containing all the longer words from the given list of words.
In the given assert statement, we are testing the function long_words with the