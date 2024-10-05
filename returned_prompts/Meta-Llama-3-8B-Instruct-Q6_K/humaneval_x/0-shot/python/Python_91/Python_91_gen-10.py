```
def is_bored(S):
    boredom_count = 0
    sentence = ""
    for char in S:
        if char in ['.', '?', '!']:
            if sentence and sentence.startswith('I'):
                boredom_count += 1
            sentence = ""
        else:
            sentence += char
    if sentence and sentence.startswith('I'):
        boredom_count += 1
    return boredom_count
```


This function iterates over the input string, building up a sentence as it goes. When it encounters a period, question mark, or exclamation point, it checks if the sentence starts with 'I'. If it does, it increments the boredom count. After processing each character, it resets the sentence. At the end, it checks one last time if the sentence starts with 'I'. If it does, it increments the boredom count. The function then returns the boredom count.