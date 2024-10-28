```
def anti_shuffle(s):
    words = s.split()
    result = []
    for word in words:
        result.append(''.join(sorted(word)))
    return ' '.join(result)
```
In this solution, we first split the input string into words using the `split` method. Then, for each word, we sort its characters using the `sorted` function and join them back into a string using the `join` method. Finally, we join the sorted words back into a string with spaces in between using the `join` method.

For example, if we call `anti_shuffle('Hello World!!!')`, the function will return `'Hello !!!Wdlor'`, which is the desired output. The function maintains the original order of words and blank spaces in the sentence.