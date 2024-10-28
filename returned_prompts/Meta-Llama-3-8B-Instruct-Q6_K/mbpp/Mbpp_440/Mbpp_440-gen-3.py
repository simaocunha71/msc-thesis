```
import re
def find_adverb_position(sentence):
    adverbs = ['quickly', 'slowly', 'loudly', 'softly', 'silently', 'clearly', 'quietly', 'noisily', 'gently', 'roughly', 'smoothly']
    for adverb in adverbs:
        if re.search(adverb, sentence):
            return re.search(adverb, sentence).start(), re.search(adverb, sentence).end(), adverb
    return -1, -1, ''
```


This function uses the `re` module in Python to search for adverbs in a sentence. It iterates over a list of common adverbs and uses the `re.search` function to find the first occurrence of each adverb in the sentence. If an adverb is found, it returns the start and end positions of the adverb, as well as the adverb itself. If no adverb is found, it returns -1, -1, and an empty string. The unit test `assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')` ensures that the function works correctly.