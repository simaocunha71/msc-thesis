The goal of this question is to break down the string into a list of words, and then return that list. Here are a few steps to accomplish this:

1. First, check if the string contains whitespaces. If it does, split the string on whitespaces and return the resulting list.
2. If no whitespaces are found, check if commas are present. If they are, split the string on commas and return the resulting list.
3. If neither whitespaces nor commas are found, we must find the number of lower-case letters with an odd order in the alphabet. We can start by initializing a counter variable to 0. Then, iterate through each character in the string. If the character is a lower-case letter and its corresponding position in the alphabet is odd (e.g., 'b' is at position 2, which is even, while 'c' is at position 3, which is odd), increment the counter by 1.
4. Finally, return the counter variable as the result.

Here's an implementation of the solution in Python:

```python
def split_words(txt):
    # Check if the string contains whitespaces
    if " " in txt:
        return txt.split(" ")

    # Check if the string contains commas
    elif "," in txt:
        return txt.split(",")

    # If no whitespaces or commas are found, count the number of lower-case letters with odd order in the alphabet
    else:
        counter = 0
        for char in txt:
            if char.islower() and ord(char) % 2 != 0:
                counter += 1
        return counter
```

This implementation uses the `split()` method to split the string on whitespaces or commas. It also uses the `ord()` function to get the ASCII value of a character, and the `islower()` method to check if a character is lowercase.

You can now use the `split_words()` function to split any given string into a list of words, or to find the number of lower-case letters with odd order in the alphabet.

```python
print(split_words("Hello world!"))  # Output: ["Hello", "world!"]
print(