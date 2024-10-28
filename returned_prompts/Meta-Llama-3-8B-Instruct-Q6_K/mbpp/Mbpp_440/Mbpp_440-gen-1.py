```
import re

def find_adverb_position(sentence):
    adverbs = ['quickly', 'slowly', 'loudly', 'silently', 'happily', 'unhappily', 'honestly', 'clearly', 'wisely', 'foolishly']
    pattern = r'\b(' + '|'.join(adverbs) + r')\b'
    match = re.search(pattern, sentence.lower())
    if match:
        return (match.start(), match.end(), match.group())
    return None
```
The function `find_adverb_position` takes a sentence as input and returns the position of the first adverb found in the sentence. If no adverb is found, it returns `None`. The adverbs are defined in the list `adverbs`. The pattern used in the regular expression is a word boundary followed by any of the adverbs in the list, followed by another word boundary. The `re.search` function is used to search for the first occurrence of the pattern in the sentence. The position of the match is returned as the start and end positions of the match, and the matched adverb is returned as the third value in the tuple. The `lower` method is used to convert the sentence to lowercase to make the search case-insensitive. The unit test `assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')` ensures that the function works correctly. 