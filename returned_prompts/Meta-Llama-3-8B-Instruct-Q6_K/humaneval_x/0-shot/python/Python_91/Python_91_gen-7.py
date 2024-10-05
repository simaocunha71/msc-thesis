```
def is_bored(S):
    sentences = S.split('. ')
    boredom_count = 0
    for sentence in sentences:
        if sentence.startswith('I'):
            boredom_count += 1
    return boredom_count
```



This Python function takes a string of words as input and returns the number of "boredoms" (i.e., sentences that start with the word "I") in the string. It does this by splitting the string into individual sentences using the '. ' character as a delimiter, then iterating over each sentence and checking if it starts with the word "I". If it does, it increments a counter. Finally, it returns the count of boredoms.

For example, if the input string is "The sky is blue. The sun is shining. I love this weather", the function will return 1, because there is one sentence that starts with the word "I". If the input string is "Hello world", the function will return 0, because there are no sentences that start with the word "I".