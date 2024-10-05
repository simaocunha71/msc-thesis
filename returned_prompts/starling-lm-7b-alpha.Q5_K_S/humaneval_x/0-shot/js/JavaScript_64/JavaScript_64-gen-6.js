
To solve this problem we need to follow the steps below:

1. Initialize a variable to store the count of vowels, say `vowelCount`.
2. Loop over the string `s`.
3. For each character in the string, check if it is a vowel.
4. If it's a vowel increment the `vowelCount`.
5. After the loop, return the `vowelCount`.

Here's the Python implementation of the above steps:

```python
def vowelsCount(s):
    vowelCount = 0
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    for char in s:
        if char in vowels:
            vowelCount += 1
    return vowelCount
```

The time complexity of this solution is O(n) where n is the length of the string.


In order to solve the problem using recursive approach, we can follow the steps below:

1. If the length of the string is 0, return 0.
2. If the first character of the string is a vowel, return 1 plus the result of the recursive call on the rest of the string.
3. Otherwise, return the result of the recursive call on the rest of the string.

Here's the Python implementation of the above steps:

```python
def vowelsCount(s):
    if len(s) == 0:
        return 0
    elif s[0] in 'aeiouy':
        return 1 + vowelsCount(s[1:])
    else:
        return vowelsCount(s[1:])
```

The time complexity of this solution is O(n) where n is the length of the string.






















































































