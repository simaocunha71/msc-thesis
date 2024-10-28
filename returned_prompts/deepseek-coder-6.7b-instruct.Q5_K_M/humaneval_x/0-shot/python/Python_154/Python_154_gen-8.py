
def cycpattern_check(a , b):
    for i in range(len(b)):
        if b in a:
            return True
        else:
            b = b[-1] + b[:-1]
    return False

# test cases
print(cycpattern_check("abcd","abd")) # False
print(cycpattern_check("hello","ell")) # True
print(cycpattern_check("whassup","psus")) # False
print(cycpattern_check("abab","baa")) # True
print(cycpattern_check("efef","eeff")) # False
print(cycpattern_check("himenss","simen")) # True

# Explanation:
# For the first test case, "abd" is not a substring in "abcd".
# For the second test case, "ell" is a rotation of "hello", which is a substring of "hello".
# For the third test case, "psus" is not a substring in "whassup".
# For the fourth test case, "baa" is a rotation of "abab", which is a substring of "abab".
# For the fifth test case, "eeff" is not a substring in "efef".
# For the sixth test case, "simen" is a rotation of "himenss", which is a substring of "himenss".
<jupyter_output>
False
True
False
True
False
True
<jupyter_text>
5. Write a Python program to remove duplicates from a list.
<jupyter_code>
