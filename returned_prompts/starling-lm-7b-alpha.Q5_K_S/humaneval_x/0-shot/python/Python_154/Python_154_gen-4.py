
def cycpattern_check(a, b):
    for i in range(len(b)):
        if b.startswith(b[i:]):
            return True
    return False

cycpattern_check("abcd","abd")
cycpattern_check("hello","ell")
cycpattern_check("whassup","psus")
cycpattern_check("abab","baa")
cycpattern_check("efef","eeff")
cycpattern_check("himenss","simen")




def cycpattern_check(a, b):
    if b.startswith(b[1:]):
        return True
    for i in range(len(b)):
        if b.startswith(b[i:]):
            return True
    return False

cycpattern_check("abcd","abd")
cycpattern_check("hello","ell")
cycpattern_check("whassup","psus")
cycpattern_check("abab","baa")
cycpattern_check("efef","eeff")
cycpattern_check("himenss","simen")




def cycpattern_check(a, b):
    return b in a or b in a[1:] + a[:1] or b in a[2:] + a[:2]

cycpattern_check("abcd","abd")
cycpattern_check("hello","ell")
cycpattern_check("whassup","psus")
cycpattern_check("abab","baa")
cycpattern_check("efef","eeff")
cycpattern_check("himenss","simen")




def cycpattern_check(a, b):
    return b in a or b in a[:-1] + a[1:] or b in a[1:-1] + a[:1] + a[-1:]

cycpattern_check("abcd","abd")
cycpattern_check("hello","ell")
cycpattern_check("whassup","psus")
cycpattern_check("abab","baa")
cycpattern