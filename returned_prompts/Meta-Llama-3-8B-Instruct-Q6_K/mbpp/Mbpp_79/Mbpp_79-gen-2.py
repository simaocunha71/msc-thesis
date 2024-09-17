```
def word_len(word):
    return len(word) % 2 != 0
```


This function takes a word as an input and returns `True` if the length of the word is odd and `False` if the length is even. The `%` operator is used to find the remainder of the division of the length of the word by 2. If the remainder is not equal to 0, then the length of the word is odd. 

The unit test `assert word_len("Hadoop") == False` ensures that the function works correctly, as the length of the word "Hadoop" is even. If the function were to return `True` for this input, the test would fail. 





