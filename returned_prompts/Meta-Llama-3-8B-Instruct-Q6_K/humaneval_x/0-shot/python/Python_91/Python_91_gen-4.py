```
def is_bored(S):
    sentences = S.split('. ')
    boredoms = [sentence for sentence in sentences if sentence and sentence.strip().lower().startswith('i')]
    return len(boredoms)
```



The function `is_bored` takes a string `S` as input and returns the number of boredoms in the string. A boredom is defined as a sentence that starts with the word "I". Sentences are delimited by '.', '?' or '!'.

The function first splits the input string into sentences using the `split` method with '. ' as the separator. This gives a list of sentences.

Then, it uses a list comprehension to filter the list of sentences and select only those that start with the word "I". The `strip` method is used to remove any leading or trailing whitespace from the sentence, and the `lower` method is used to convert the sentence to lowercase so that the comparison is case-insensitive.

Finally, the function returns the length of the list of boredoms, which is the number of sentences that start with the word "I".