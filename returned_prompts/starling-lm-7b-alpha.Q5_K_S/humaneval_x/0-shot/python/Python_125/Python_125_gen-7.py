In the `split_words` function, we check if the string contains whitespace or commas. If it does, we use the `split()` method to split the string into a list of words. If not, we iterate through the string and count the number of lower-case letters with odd order in the alphabet.

Here's a step-by-step explanation of the solution:

1. Check if the string contains whitespace or commas:
   - If it does, use the `split()` method to split the string into a list of words.
   - If it doesn't, proceed to the next step.

2. Iterate through the string and count the number of lower-case letters with odd order in the alphabet:
   - Initialize a variable `count` to keep track of the count.
   - Iterate through each character in the string.
   - Check if the character is a lower-case letter and its ordinal value is odd.
   - If both conditions are true, increment the `count` by 1.

3. Return the count if no whitespaces or commas are found in the string. Otherwise, return the list of words.

Note: The `ord()` function is used to get the Unicode code point of a character.

Here's the modified code with comments explaining each step:

```python
def split_words(txt):
    # Check if the string contains whitespace or commas
    if ' ' in txt or ',' in txt:
        # If it does, use the split() method to split the string into a list of words
        return txt.split()
    else:
        # Initialize a variable to keep track of the count
        count = 0
        # Iterate through each character in the string
        for char in txt:
            # Check if the character is a lower-case letter and its ordinal value is odd
            if char.islower() and ord(char) % 2 != 0:
                # If both conditions are true,