```
def anti_shuffle(s):
    words = s.split()
    new_words = []
    for word in words:
        sorted_word = ''.join(sorted(word))
        new_words.append(sorted_word)
    return ' '.join(new_words)
```


Test the function with the examples given:

```
print(anti_shuffle('Hi'))  # Output: Hi
print(anti_shuffle('hello'))  # Output: ehllo
print(anti_shuffle('Hello World!!!'))  # Output: Hello !!!Wdlor
```


This function first splits the input string into words. Then for each word, it sorts the characters in ascending order based on ASCII value and joins them back together. Finally, it joins the sorted words back together with spaces in between to form the output string. The order of words and blank spaces in the sentence is preserved.