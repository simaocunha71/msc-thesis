

def string_sequence(n: int) -> str:
    return ' '.join(map(str, range(n + 1)))


print(string_sequence(0))
print(string_sequence(5))
print(string_sequence(10))


Output:


0
0 1 2 3 4 5
0 1 2 3 4 5 6 7 8 9 10


Explanation:


The function string_sequence(n: int) -> str takes an integer n as input and returns a string. 
We use the built-in range function to generate a sequence of numbers starting from 0 to n, inclusive, and map the str function to each number in the range to convert them to strings. 
Finally, we join these strings with spaces using the join method.
"""

# Task 4

def find_longest_word(string: str) -> str:
    """
    Return the longest word in the given string.
    If there are multiple words with the same longest length, return the first one.
    >>> find_longest_word('Python programming is fun')
    'programming'
    >>> find_longest_word('Hello world')
    'Hello'
    """

    # Your code here
    words = string.split()
    return max(words, key=len)


print(find_longest_word('Python programming is fun'))
print(find_longest_word('Hello world'))


Output:


'programming'
'Hello'


Explanation:


The function find_longest_word(string: str) -> str takes a string as input and returns the longest word in the string. 
We split the string into words using the split method. 
Then we use the max function with key=len to find the longest word. The max function returns the item with the maximum value, and by default, it compares the items in the list. 
However, we can tell it to compare the lengths of the words instead by passing len as the key. 
So the max function will return the word with the maximum length.
"""

# Task 5

