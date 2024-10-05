
```
def split_words(txt):
    words = txt.split()
    if not words:
        words = txt.replace(',', ' ').split()
        if not words:
            return sum(1 for i in range(ord('a'), ord('z')+1) if txt.lower().count(chr(i)) % 2 != 0)
    return words
```

Explanation:

1. The function `split_words(txt)` takes a string `txt` as input.
2. It first splits the string into words using the `split()` method with no arguments, which splits on whitespace.
3. If the resulting list of words is empty, it means there were no whitespace characters in the original string, so it replaces all commas with spaces using the `replace()` method and then splits the string again.
4. If the resulting list of words is still empty, it means there were no whitespace or commas in the original string, so it counts the number of lower-case letters with odd order in the alphabet using a generator expression.
5. Finally, it returns the list of words or the count of lower-case letters with odd order in the alphabet, depending on whether the original string contained whitespace or not.

Note: The `ord()` function is used to get the ASCII value of a character, and the `chr()` function is used to get the character represented by a specific ASCII value. The `range()` function is used to generate a sequence of numbers from `ord('a')` to `ord('z')`. The `count()` method is used to count the number of occurrences of a character in