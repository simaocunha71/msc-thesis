```
def split_words(txt):
    words = txt.split()
    if len(words) > 0:
        return words
    else:
        words = txt.replace(',', ' ')
        words = words.split()
        if len(words) > 0:
            return words
        else:
            return sum(1 for i in range(26) if chr(i + ord('a')).lower() in txt and (i + ord('a')) % 2 == 1)
``` 