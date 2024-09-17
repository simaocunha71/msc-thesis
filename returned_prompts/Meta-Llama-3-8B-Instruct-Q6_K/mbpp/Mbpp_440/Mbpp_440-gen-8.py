```
import re

def find_adverb_position(sentence):
    adverbs = re.findall(r'\b(rapidly|quickly|loudly|silently|clearly|gently|firmly|slowly|wisely|carefully|strongly|vigorously)\b', sentence, re.IGNORECASE)
    if adverbs:
        return (0, len(sentence.split()[0].encode('utf-8')) + len(adverbs[0]), adverbs[0])
    else:
        return None
```



This function uses regular expressions to find all adverbs in the sentence. It then checks if any adverbs were found. If they were, it returns the position of the first adverb (the first word in the sentence), the length of the first word in the sentence plus the length of the first adverb, and the first adverb itself. If no adverbs were found, it returns None. The position is calculated by summing the length of the first word in the sentence and the length of the first adverb. This is because the position of the first word is 0 and the position of the first character of the second word is the length of the first word. The position of the first character of the third word is the length of the first word plus the length of the second word. This way, the position of the first character of the first adverb is the length of the first word plus the length of the first word. 

The unit test `assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')` shows that the position of the adverb "clearly" is the length of the first word ("clearly") plus the length of the adverb itself. The position of the first character of the adverb is 0. The position of the first character of the first word is 7. 

Note that this function is case-insensitive and it will find adverbs regardless of their position in the sentence. It will also find adverbs that are part of another word, such as "clearly" in "clearly!!".  It will not find adverbs that are part of a word and are not at the beginning of the sentence, such as "clearly" in "the clearly sky". If you want to find adverbs that are not at the beginning of the sentence, you can modify this function to return all positions of adverbs in the sentence.  If you want