
def cycpattern_check(a,b):
    if b in a:
        return True
    else:
        for i in range(len(b)):
            if b[i:]+b[:i] in a:
                return True
    return False

cycpattern_check("abcd","abd") # False
cycpattern_check("hello","ell") # True
cycpattern_check("whassup","psus") # False
cycpattern_check("abab","baa") # True
cycpattern_check("efef","eeff") # False
cycpattern_check("himenss","simen") # True



# Another solution

def cycpattern_check(a, b):
    for i in range(len(b)):
        if b[i:]+b[:i] in a:
            return True
    return False
cycpattern_check("abcd","abd") # False
cycpattern_check("hello","ell") # True
cycpattern_check("whassup","psus") # False
cycpattern_check("abab","baa") # True
cycpattern_check("efef","eeff") # False
cycpattern_check("himenss","simen") # True


# Another solution

def cycpattern_check(a, b):
    b = b + b
    return b in a
cycpattern_check("abcd","abd") # False
cycpattern_check("hello","ell") # True
cycpattern_check("whassup","psus") # False
cycpattern_check("abab","baa") # True
cycpattern_check("efef","eeff") # False
cycpattern_check("himenss","simen") # True

# Another solution

def cycpattern_check(a, b):
    for i in range(len(b)):
        if b[i:]+b[:i] in a:
            return True
    return False
cycpattern_check("abcd","abd") # False
cycpattern_check("hello","ell") # True
cycpattern_check("whassup","psus