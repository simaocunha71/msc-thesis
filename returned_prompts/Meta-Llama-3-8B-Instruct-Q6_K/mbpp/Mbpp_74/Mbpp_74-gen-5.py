```
def is_samepatterns(patterns1, patterns2):
    if len(patterns1)!=len(patterns2):
        return False
    for i in range(len(patterns1)):
        if patterns1[i] != patterns2[i]:
            return False
    return True
```
The function compares the two lists of patterns. If the lengths of the lists are different, it returns False. If the lists are of the same length, it iterates over the lists and checks if each pair of elements is equal. If it finds a pair that is not equal, it returns False. If it does not find any unequal pairs, it returns True. This function is used to check whether a sequence of colors follows a sequence of patterns. 

The unit test `assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True` ensures that the function works correctly. If the sequence of colors is `["red","green","green"]` and the sequence of patterns is `["a", "b", "b"]`, the function should return True. This is because the two sequences are the same. If the two sequences were different, the function would return False. 