
def cycpattern_check(a,b):
    if b in a:
        return True
    else:
        for i in range(len(b)):
            if b[i:]+b[:i] in a:
                return True
    return False

cycpattern_check("abcd","abd") # returns False
cycpattern_check("hello","ell") # returns True
cycpattern_check("whassup","psus") # returns False
cycpattern_check("abab","baa") # returns True
cycpattern_check("efef","eeff") # returns False
cycpattern_check("himenss","simen") # returns True


























































```
def cycpattern_check(a,b):
    if b in a:
        return True
    else:
        for i in range(len(b)):
            if b[i:]+b[:i] in a:
                return True
    return False
```