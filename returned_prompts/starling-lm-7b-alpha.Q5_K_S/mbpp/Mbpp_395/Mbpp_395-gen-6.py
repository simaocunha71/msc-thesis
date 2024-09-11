
To find the first non-repeated character in a given string, you can follow these steps:

1. Create a dictionary to store the count of each character in the string.
2. Iterate through the string and update the dictionary accordingly.
3. Iterate through the string again and check if the count of the current character is equal to 1. If so, return the character.
4. If no non-repeated character is found, return None.

Here's a Python function that implements this logic:

```python
def first_non