"""
def find_char_long(str):
    return set([word for word in str.split() if len(word) >= 4])
"""

def find_char_long(str):
    char_long = set()
    for word in str.split():
        if len(word) >= 4:
            char_long.add(word)
    return char_long

# assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])




"""
The above code works by splitting the string into a list of words, then going through the list and adding each word to the set if its length is 4 or more.
The function returns the set of words.
"""


























"""
Here's some additional information about the function and the problem:

In this problem, we are asked to find all words in a string that are at least 4 characters long. To solve this problem, we can follow these steps:

1. Split the string into a list of words using the split() function. This will give us a list of words.
2. Initialize an empty set called char_long. A set is a collection of unique elements. We will use a set to store the words that are at least 4 characters long.
3. Iterate through each word in the list of words. For each word, we can check if its length is greater than or equal to 4 using the len() function. If the length of the word is 4 or more, we can add the word to the char_long set using the add() method.
4. After iterating through all the words, we can return the char_long set, which will contain all the words that are at least 4 characters long.

By following these steps, we can solve the problem and find all the words in the string that are at least 4 characters long.

The assert statement at the end of the code is used to check if the function is working correctly. It compares the set of words returned by the function with the expected set of words, and if they are equal, it means the function is working correctly.
"""




