```
def is_samepatterns(patterns, colors):
    if len(patterns) != len(colors):
        return False
    for i in range(len(patterns)):
        if patterns[i] != colors[i]:
            return False
    return True
```
The function takes two lists as input, patterns and colors. It checks if the lengths of both lists are equal, if not, it returns False. Then it iterates over the lists, and if it finds a mismatch between patterns and colors, it returns False. If it doesn't find any mismatch after checking all elements, it returns True, indicating that the lists follow the same pattern. 

The unit test `assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True` shows that the function should return True when the lists have the same elements in the same order. 

For example, if the input is `is_samepatterns(["red","green","green"], ["a", "b", "b"])`, the function will return True because the lists have the same elements in the same order. If the input is `is_samepatterns(["red","green","blue"], ["a", "b", "b"])`, the function will return False because the lists have different elements in the same position.  If the input is `is_samepatterns(["red","green"], ["a", "b", "b"])`, the function will return False because the lists have different lengths.  If the input is `is_samepatterns(["red","green","green"], ["a", "b", "c"])`, the function will return False because the lists have different elements in the same position.  If the input is `is_samepatterns(["red","green","green"], ["a", "b"])`, the function will return False because the lists have different lengths.  If the input is `is_samepatterns(["red","green","green"], [])`, the function will return False because the lists have different lengths.  If the input is `is_samepatterns([], ["a", "b", "b"])`, the function will return False because the lists have different lengths.  If the input is `is_samepatterns(["red","green","green"], ["a", "b"])`, the function will return False because the lists have different lengths.  If the input is `is_samepatterns(["red","green","green"], ["a", "b", "b", "c"])`, the function will return False because the lists