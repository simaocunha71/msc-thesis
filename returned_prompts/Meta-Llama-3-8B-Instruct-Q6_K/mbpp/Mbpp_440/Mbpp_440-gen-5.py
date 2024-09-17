```
import re
import string

def find_adverb_position(sentence):
    adverbs = ['quickly', 'loudly', 'clearly', 'brightly', 'slowly', 'silently', 'quietly', 'gently', 'bravely', 'boldly']
    adverb = None
    position = None
    for i, word in enumerate(re.split(r'\W+', sentence)):
        if word.lower() in [a.lower() for a in adverbs]:
            adverb = word
            position = i
            break
    return position, position + len(adverb), adverb
```

The function `find_adverb_position` takes a sentence as input and returns the position of the first adverb and the adverb itself. 

It uses regular expression to split the sentence into words and then checks each word to see if it is an adverb. If it is, the function returns the position of the adverb, the position of the adverb plus the length of the adverb, and the adverb itself.

The unit test `assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')` ensures that the function works correctly. It checks if the position of the first adverb is 0, the position of the adverb plus the length of the adverb is 7, and the adverb itself is 'clearly'. 

This function is case-insensitive, so it will find adverbs regardless of their case in the sentence. 

Please note that this function does not handle punctuation attached to the adverb. For example, if the adverb is 'clearly!!', the function will consider it as two separate words, 'clearly' and '!!'. If you want to handle punctuation attached to the adverb, you will need a more complex approach. 

Also, this function only checks for a limited set of adverbs. If you want to check for all adverbs, you will need a more comprehensive list of adverbs. 

Finally, this function assumes that the input is a sentence. If the input is not a sentence, the function may not work correctly. 





This function is case-insensitive, so it will find adverbs regardless of their case in the sentence. 

Please note that this function does not handle punctuation attached to the adverb. For example, if the adverb is 'clearly!!', the function will consider it as two separate words, '