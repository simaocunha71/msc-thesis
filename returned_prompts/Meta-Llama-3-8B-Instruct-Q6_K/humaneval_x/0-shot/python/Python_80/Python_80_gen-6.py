```
def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(0, len(s), 3):
        chunk = s[i:i+3]
        if len(set(chunk)) < 3:
            return False
    return True
```


Explanation:
The function `is_happy(s)` takes a string `s` as input and checks if it's happy or not.

1. First, it checks if the length of the string is less than 3. If it is, it returns `False` because a happy string must have a length of at least 3.

2. Then, it iterates over the string in chunks of 3 characters using a for loop. For each chunk, it converts the chunk into a set (which removes duplicate characters) and checks if the size of the set is less than 3. If it is, it means that there are duplicate characters in the chunk, so it returns `False`.

3. If the function hasn't returned `False` after checking all chunks, it means that the string is happy, so it returns `True`.