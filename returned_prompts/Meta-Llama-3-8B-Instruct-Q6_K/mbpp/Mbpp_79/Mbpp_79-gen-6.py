You can use the built-in modulus operator (%) in Python to find the remainder of the division of the length of the word by 2. If the remainder is 0, the length of the word is even, otherwise, it's odd.

Here is the Python function to check whether the length of the word is odd or not:

```Python
def word_len(word):
    return len(word) % 2 != 0
```

This function takes a word as an input, calculates its length using the len() function, and then checks if the remainder of the division of the length by 2 is not equal to 0. If it's not equal to 0, it returns True, indicating that the length of the word is odd. Otherwise, it returns False, indicating that the length of the word is even. 

The unit test `assert word_len("Hadoop") == False` ensures that the function works correctly, as the length of the word "Hadoop" is 6, which is even. Therefore, the function should return False for this word. 












