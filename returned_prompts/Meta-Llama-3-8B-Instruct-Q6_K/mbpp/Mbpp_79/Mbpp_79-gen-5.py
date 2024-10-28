```
def word_len(word):
    return len(word) % 2 != 0
```
In this function, we are using the modulus operator `%` to find the remainder of the word length when divided by 2. If the remainder is not equal to 0, then the length of the word is odd, and the function returns `True`. Otherwise, it returns `False`. The unit test `assert word_len("Hadoop") == False` ensures that the function correctly identifies the length of the word "Hadoop" as even.