```python

def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    from collections import Counter
    def check(a, b):
        if Counter(a) != Counter(b):
            return False
        else:
            return True
    for i in range(len(b)):
        if check(a, b[i:]+b[:i]):
            return True
    return False


```
