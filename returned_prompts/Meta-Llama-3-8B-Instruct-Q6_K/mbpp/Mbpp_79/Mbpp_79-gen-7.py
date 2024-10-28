```
def word_len(word):
    return len(word) % 2 != 0
```
In this function, we are using the modulus operator `%` to find the remainder of the word's length when divided by 2. If the remainder is not 0, it means the length is odd, and we return `True`. If the remainder is 0, it means the length is even, and we return `False`. The unit test `assert word_len("Hadoop") == False` confirms that the function works correctly, as the length of the word "Hadoop" is even. 







