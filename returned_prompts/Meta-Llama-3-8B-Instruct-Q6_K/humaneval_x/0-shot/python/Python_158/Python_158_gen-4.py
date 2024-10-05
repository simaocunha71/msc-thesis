```
def find_max(words):
    max_word = max(words, key=lambda x: (len(set(x)), x))
    return max_word
```
The problem asks for a function that takes a list of strings as input and returns the string with the maximum number of unique characters. If there are multiple strings with the same maximum number of unique characters, the function should return the one that comes first in lexicographical order.

We can solve this problem by using the built-in `max` function in Python, along with the `key` argument. The `key` argument allows us to specify a function that will be used to determine the maximum value.

In this case, we'll use a lambda function that returns a tuple. The first element of the tuple is the length of the set of unique characters in the string, and the second element is the string itself.

The `max` function will return the string with the maximum length of unique characters. If there are multiple strings with the same maximum length of unique characters, it will return the one that comes first in lexicographical order.

Here's the solution:
```
def find_max(words):
    max_word = max(words, key=lambda x: (len(set(x)), x))
    return max_word
```
This function takes a list of strings as input, finds the string with the maximum number of unique characters, and returns that string. If there are multiple strings with the same maximum number of unique characters, it returns the one that comes first in lexicographical order.