```
def is_bored(S):
    sentences = S.split('. ') + S.split('? ') + S.split('! ')
    boredoms = [sentence for sentence in sentences if sentence and sentence[0].lower() == 'i']
    return len(boredoms)
```



Python code that counts the number of "boredoms" in a given string. A "boredom" is a sentence that starts with the word "I".

The `is_bored` function takes a string `S` as input. It first splits the string into sentences using the `split` method with `'. '`, `'?'`, and `'!'` as delimiters. It then creates a list comprehension to filter out sentences that are empty or do not start with the word "I" (case-insensitive). Finally, it returns the length of the list of "boredoms".

The unit tests provided in the problem statement demonstrate the expected behavior of the `is_bored` function. For example, the test `is_bored("Hello world")` returns `0` because there are no "boredoms" in the input string. The test `is_bored("The sky is blue. The sun is shining. I love this weather")` returns `1` because there is one "boredom" in the input string.