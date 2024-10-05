
def cycpattern_check(a, b):
    for i in range(len(b)):
        if b in a:
            return True
        b = b[-1:] + b[:-1]
    return False

print(cycpattern_check("abcd","abd"))
print(cycpattern_check("hello","ell"))
print(cycpattern_check("whassup","psus"))
print(cycpattern_check("abab","baa"))
print(cycpattern_check("efef","eeff"))
print(cycpattern_check("himenss","simen"))

# This program checks if any rotation of the second string is a substring of the first string. It does this by rotating the second string and checking if it is a substring of the first string. If any rotation of the second string is a substring of the first string, the function returns True. Otherwise, it returns False.
<jupyter_output>
False
True
False
True
False
True
<jupyter_text>
