
def cycpattern_check(a,b):
    return any(b in a or b in a[i:] + a[:i] for i in range(len(a)))

# cycpattern_check("abcd","abd") => False
# cycpattern_check("hello","ell") => True
# cycpattern_check("whassup","psus") => False
# cycpattern_check("abab","baa") => True
# cycpattern_check("efef","eeff") => False
# cycpattern_check("himenss","simen") => True





def cycpattern_check(a,b):
    return any(b in a or b in a[i:] + a[:i] for i in range(len(a)))

# cycpattern_check("abcd","abd") => False
# cycpattern_check("hello","ell") => True
# cycpattern_check("whassup","psus") => False
# cycpattern_check("abab","baa") => True
# cycpattern_check("efef","eeff") => False
# cycpattern_check("himenss","simen") => True





```
Here is one way to solve this problem.
The idea of the solution is to rotate the string `b` and check if it is a substring of the string `a`.
To rotate the string `b`, we can use slicing in Python. For example, if `b` is `'ab'`, then `b[1:] + b[:1]` will be `'ba'`.
We need to check if `b` is a substring of `a` or if `b` is a substring of `a[i:] + a[:i]` for any `i` in the range of the length of `a`.
For example, if `a` is `'abcd'` and `b` is `'abd'`, then `b` is a substring of `a`.
If `b` is `'abd'`, then `b` is a substring of `a` and `a[1:] + a[:1]`, which means that