
import re

def select_words(s, n):
    words = []
    for word in re.split(' ', s):
        if len(re.findall('[aeiou]', word)) == n:
            words.append(word)
    return words
