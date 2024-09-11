Here's one possible solution:

```python
def capital_words_spaces(s):
    # First, we define a list of all capital letters
    capital_letters = [chr(x) for x in range(65, 91)]
    # Then we iterate over the string, and if the first letter of the word is a capital letter,
    # we add a space before the word
    result = ""
    prev_capital = False
    for i in range(len(s)):
        if i == 0 or s[i-1] == " ":
            result += s[i]
        elif capital_letters.__contains__(s[i]):
            result += " " + s[i]
        else:
            result += s[i]
            prev_capital = True
    return result
```

Here's an example of how to use the function:

```python
print(capital_words_spaces("Python"))  # prints: Python
print(capital_words_spaces("JavaScript"))  # prints: Java Script
```

This function works by iterating over each character in the string, and if the character is a capital letter, it adds a space before it. If the character is not a capital letter, it adds the character to the result string without adding any spaces. It also keeps track of whether the previous character was a capital letter, so that it doesn't add a space before the first word in the string.

Note that this function is case-sensitive, so it will not add spaces before lowercase letters that are the first letter of a word, only capital letters.

If you need a solution that is case-insensitive, you can modify the function to convert the input string to lowercase before processing it. Here's an example of how to do that:

```python
def capital_words_spaces(s):
    # Convert the input string to lowercase
    s = s.lower()
    # Rest of the function is the same as before
```

This version of the function will add spaces before all capital letters, regardless of whether they are uppercase or lowercase.

```python
print(capital_words_spaces("Python"))