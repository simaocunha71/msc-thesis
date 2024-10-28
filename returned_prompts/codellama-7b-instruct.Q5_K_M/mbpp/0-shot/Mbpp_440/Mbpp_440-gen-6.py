
```
def find_adverb_position(sentence):
    adverbs = ['quickly', 'quick', 'fast', 'soon', 'clearly', 'well', 'badly', 'good', 'goodly', 'goodness', 'well', 'well', 'well']
    for i, word in enumerate(sentence.split()):
        if word in adverbs:
            return i, len(word), word
    return -1, -1, 'NA'
```


