"""
Write a function to find the first adverb and their positions in a given sentence.
assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
"""
import re
from collections import Counter
def find_adverb(string):
    pattern = r'[a]dverbs' #finds all adverbs and adds them to a list
    re_list = [re.compile(pattern) for _ in range(len(string))]

    count = 1
    for i, re_match in enumerate(re_list):
        adverb = re_match.findall(string)[0]
        if adverb and count > 0:
            return (i, i+adverb[::-1].count('a')-1, adverb)
        else:
            print("No adverb found in the sentence")
    return None

def find_adverb_position(string):
    adverbs = [find_adverb(s[:i] + s[i+1:]) for i, s in enumerate(string.split()) if isinstance(find_adverb(s), tuple)]
    return sorted(enumerate(adverbs), key=lambda x: x[-2], reverse=True)

assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
assert find_adverb_position("I'm clearly an adverb. This is not a sentence, yet.") == (11, 12, 'clearly')