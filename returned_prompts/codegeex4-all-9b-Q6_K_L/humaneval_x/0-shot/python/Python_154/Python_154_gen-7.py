def cycpattern_check(a , b):
    return any(b in a[i:] + a[:i] for i in range(len(b)))

print cycpattern_check("abcd","abd") # False
print cycpattern_check("hello","ell") # True
print cycpattern_check("whassup","psus") # False
print cycpattern_check("abab","baa") # True
print cycpattern_check("efef","eeff") # False
print cycpattern_check("himenss","simen") # True