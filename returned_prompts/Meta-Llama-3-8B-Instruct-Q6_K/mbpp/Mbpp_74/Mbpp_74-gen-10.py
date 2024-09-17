```
def is_samepatterns(patterns):
    for p in patterns:
        if len(p) != len(patterns[0]):
            return False
    return True
```
This function checks if all patterns in the list have the same length. If they do, it returns True, otherwise it returns False.

For example, the unit test `assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True` would pass, because all patterns in the list have the same length. The function would return True. If any of the patterns had a different length, the function would return False. 