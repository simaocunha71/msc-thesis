```
import re
from collections import namedtuple

AdverbPosition = namedtuple('AdverbPosition', ['start', 'end', 'adverb'])

def find_adverb_position(sentence):
    adverbs = ['clearly', 'quickly', 'loudly', 'slowly', 'silently', 'quietly']
    for adverb in adverbs:
        match = re.search(r'\b' + re.escape(adverb) + r'\b', sentence)
        if match:
            return AdverbPosition(start=match.start(), end=match.end(), adverb=adverb)
    return None
```
In this solution, we first import the necessary modules. We use the `re` module for regular expressions and the `namedtuple` function from the `collections` module to create a custom named tuple for storing the adverb position.

We define a list of adverbs that we want to find in the sentence. Then, we iterate over each adverb in the list. For each adverb, we use a regular expression to search for the adverb in the sentence. The regular expression `\b` matches a word boundary, and `re.escape(adverb)` escapes any special characters in the adverb. The `search` method returns a match object if the adverb is found, or `None` if it's not.

If the adverb is found, we create an `AdverbPosition` object with the start and end positions of the match, and return it. If no adverbs are found, we return `None`.

The unit test `assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')` ensures that the function returns the correct adverb position for the given sentence. The expected output is `(0, 7, 'clearly')`, which means the adverb 'clearly' starts at position 0 and ends at position 7 in the sentence.