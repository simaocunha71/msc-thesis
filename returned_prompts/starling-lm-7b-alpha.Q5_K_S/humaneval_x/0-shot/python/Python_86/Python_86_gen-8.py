
Here is one possible solution to the problem:

```python
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # Split the string into words
    words = s.split(' ')

    # Create a new string with each word replaced by an ordered version of itself
    ordered_s = ' '.join(
        ''.join(sorted([char for char in word]))
        for word in words
    )

    return ordered_s
```

This solution works by splitting the input string into a list of words. Then, for each word in the list, it creates a new word by sorting the characters in the word in ascending order based on their ASCII values. Finally, it joins all the words back together with spaces between them to form the output string.

For example, if you call `anti_shuffle('Hello World!!!')`, the function will split the string into the words `['Hello', 'World', '!!', '!', 'a', 'd', 'l', 'l', 'o', 'o', 'r', 'W']`. It will then sort the characters in each word to get the ordered words `['Hello', 'Wdlor', '!!', 'a', 'd', 'l', 'l', 'o', 'o', 'r', '!']`. Finally, it will join these words back together with spaces to get the output string `'Hello !!!Wdlor a d l l o o r !'`.

I hope this helps! Let me know if you have any more questions.

```python
```

Here is one possible solution to the problem:

```python
def anti_sh