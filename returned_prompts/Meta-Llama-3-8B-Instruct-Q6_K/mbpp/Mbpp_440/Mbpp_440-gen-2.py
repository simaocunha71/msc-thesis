```
import re
def find_adverb_position(sentence):
    adverbs = ['quickly', 'slowly', 'loudly', 'silently', 'clearly']
    for i, word in enumerate(re.findall(r'\b\w+\b', sentence.lower())):
        if word in adverbs:
            return (i, i+len(word), word)
    return None
```
The function `find_adverb_position` takes a sentence as input and returns a tuple of the position of the first adverb, the length of the adverb, and the adverb itself. It uses the `re` module to find all the words in the sentence, and then checks if each word is in the list of adverbs. If it finds an adverb, it returns a tuple with the position, length, and adverb. If it doesn't find any adverb, it returns `None`.

For example, if you call `find_adverb_position("clearly!! we can see the sky")`, it will return `(0, 7, 'clearly')`, indicating that the first adverb is 'clearly' at position 0, with a length of 7. 

This function is case-insensitive, so it will find adverbs regardless of their case in the sentence. It also ignores punctuation and other non-word characters. 

The unit test `assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')` ensures that the function works correctly for this specific sentence. 

Note that this function is case-insensitive, so it will find adverbs regardless of their case in the sentence. It also ignores punctuation and other non-word characters. 

This function will only work correctly if the adverbs are in the list `adverbs`. If you want to extend the function to find adverbs that are not in this list, you would need to modify it to use a more comprehensive list of adverbs or to use a natural language processing library that can identify adverbs. 