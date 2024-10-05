```
def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(0, len(s), 3):
        chunk = s[i:i+3]
        if len(set(chunk)) != 3:
            return False
    return True
```



Explanation:

*   The function `is_happy(s)` checks if the input string `s` is happy or not.
*   A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.
*   The function first checks if the length of the string is less than 3. If it is, the function returns `False` because a string with a length less than 3 cannot be happy.
*   Then, the function iterates over the string in chunks of 3 characters each. For each chunk, it converts the chunk into a set (which removes duplicates) and checks if the length of the set is equal to 3. If it is not, the function returns `False` because the string is not happy.
*   If the function has not returned `False` after checking all chunks, it returns `True` because the string is happy.
*   The function uses the `set` data structure to remove duplicates from the chunk, and the `len` function to check the length of the set. It also uses the `range` function to iterate over the string in chunks of 3 characters each.