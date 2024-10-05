def cycpattern_check(a , b):
    for i in range(len(b)):
        if b in a:
            return True
        b = b[-1] + b[:-1]
    return False

print(cycpattern_check("abcd","abd"))
print(cycpattern_check("hello","ell"))
print(cycpattern_check("whassup","psus"))
print(cycpattern_check("abab","baa"))
print(cycpattern_check("efef","eeff"))
print(cycpattern_check("himenss","simen"))