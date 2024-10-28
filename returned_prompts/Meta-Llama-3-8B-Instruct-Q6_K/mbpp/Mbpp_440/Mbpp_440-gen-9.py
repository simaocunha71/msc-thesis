```
import re
def find_adverb_position(sentence):
    pattern = r'\b(adv|ly|wise|well|fast|hard|quick|slow|loud|soft|bright|dark|far|near|up|down|in|out|on|off|through|under)\b'
    matches = re.finditer(pattern, sentence)
    for match in matches:
        return match.start(), match.end(), match.group()
    return None
```        
        


Test:
```
assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
```        
        


Explanation:
The problem is to write a function that finds the first adverb in a given sentence and returns its position along with the adverb itself. The adverbs are considered as any word that ends in 'ly', 'wise', 'well', 'fast', 'hard', 'quick', 'slow', 'loud', 'soft', 'bright', 'dark', 'far', 'near', 'up', 'down', 'in', 'out', 'on', 'off', 'through', or 'under'.

The function uses regular expression to find the first adverb in the sentence. The regular expression pattern is created using the `re` module. The pattern `\b(adv|ly|wise|well|fast|hard|quick|slow|loud|soft|bright|dark|far|near|up|down|in|out|on|off|through|under)\b` matches any word that ends in 'ly', 'wise', 'well', 'fast', 'hard', 'quick', 'slow', 'loud', 'soft', 'bright', 'dark', 'far', 'near', 'up', 'down', 'in', 'out', 'on', 'off', 'through', or 'under'.

The `re.finditer` function is used to find all matches of the pattern in the sentence. The `for` loop is used to iterate over the matches, and the first match is returned. If no match is found, the function returns `None`.

The test case `assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')` checks if the function returns the correct position and adverb for the sentence "clearly!! we can see the sky". The expected output is `(0, 7, 'clearly')`, which means that the