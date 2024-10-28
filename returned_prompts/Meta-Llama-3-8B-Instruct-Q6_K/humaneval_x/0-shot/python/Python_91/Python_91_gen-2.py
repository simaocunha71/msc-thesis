```
def is_bored(S):
    sentences = S.split('. ')
    boredoms = 0
    for sentence in sentences:
        if sentence and sentence[0] == 'I':
            boredoms += 1
    return boredoms
```


The function `is_bored(S)` takes a string `S` as an argument. It first splits the string into sentences using the `split('. ')` method. Then it iterates over each sentence, and checks if the sentence is not empty and starts with the word 'I'. If it does, it increments the `boredoms` counter. Finally, it returns the number of boredoms.