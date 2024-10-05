```
def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        if len([char for char in word if char.lower() not in 'aeiou']) == n:
            result.append(word)
    return result
```


The function `select_words(s, n)` takes a string `s` and a natural number `n` as input. It first splits the input string `s` into a list of words using the `split()` method. Then, it iterates over each word in the list and checks if the number of consonants (characters that are not vowels) in the word is equal to `n`. If it is, the word is added to the `result` list. Finally, the function returns the `result` list.

The list comprehension `[char for char in word if char.lower() not in 'aeiou']` is used to count the number of consonants in a word. The `if char.lower() not in 'aeiou'` part of the condition ensures that only characters that are not vowels (i.e., consonants) are included in the count. The `char.lower()` part is used to make the function case-insensitive, so that it treats uppercase and lowercase letters as the same.

For example, if `s = "Mary had a little lamb"` and `n = 4`, the function will return `["little"]` because "little" is the only word in the string that has exactly 4 consonants. If `s = "Hello world"` and `n = 4`, the function will return `["world"]` because "world" is the only word in the string that has exactly 4 consonants. If `s = "simple white space"` and `n = 2`, the function will return an empty list because there are no words in the string that have exactly 2 consonants. If `s = "Uncle sam"` and `n = 3`, the function will return `["Uncle"]` because "Uncle" is the only word in the string that has exactly 3 consonants.