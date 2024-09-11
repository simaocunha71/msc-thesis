def long_words(n,words):
    return [i for i in words.split() if len(i)>n]


"""
def long_words(n,words):
    long_word = []
    for i in words:
        if len(i)>n:
            long_word.append(i)
    return long_word
"""

print(long_words(3,"python is a programming language"))
# ['python','programming','language']


"""
def long_words(n,words):
    long_word = []
    words = words.split()
    for i in words:
        if len(i)>n:
            long_word.append(i)
    return long_word
"""
# Time: O(n)
# Space: O(n)

# Another Solution:
"""
def long_words(n,words):
    return [i for i in words.split() if len(i)>n]
"""
# Time: O(n)
# Space: O(1)

```
```
```