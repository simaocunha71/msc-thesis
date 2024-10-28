
def select_words(s, n):
    res = []
    for word in s.split():
        cnt = 0
        for c in word:
            if c not in 'aeiou':
                cnt += 1
            if cnt == n:
                res.append(word)
                break
    return res

# def select_words(s, n):
#     vowels = 'aeiou'
#     return [word for word in s.split() for c in word if c not in vowels if len([c for c in word if c not in vowels]) == n]



def select_words(s, n):
    vowels = 'aeiou'
    return [word for word in s.split() if len([c for c in word if c not in vowels]) == n]




```

In [8]:
```

```python
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """

    vowels = 'aeiou'
    return [word for word in s.split() if len([c for c in word if c not in vowels]) == n]
```
```

Here's a function `select_words` that solves the problem:

```python
def select_words(s, n):
    """G