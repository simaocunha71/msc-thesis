
def cycpattern_check(a , b):
    for i in range(len(b)):
        if b in a:
            return True
        else:
            b = b[-1:] + b[:-1]
    return False

print(cycpattern_check("abcd","abd"))  # => False
print(cycpattern_check("hello","ell"))  # => True
print(cycpattern_check("whassup","psus"))  # => False
print(cycpattern_check("abab","baa"))  # => True
print(cycpattern_check("efef","eeff"))  # => False
print(cycpattern_check("himenss","simen"))  # => True

# The function works by creating a rotation of the second string 'b' and checking if it exists in the first string 'a' for each rotation. If it does, the function returns True. If it doesn't, after the last rotation, the function returns False.

# The time complexity of the function is O(n*m), where n is the length of the first string and m is the length of the second string.

# The space complexity of the function is O(1), since it uses a fixed amount of space to store the input strings and the rotated string.

# The function assumes that the input strings are non-empty and contain only lowercase letters. It also assumes that the second string is a substring of the first string.
<jupyter_output>
False
True
False
True
False
True
<jupyter_text>
Question 3Write a function that takes two strings and returns True if the first string is a subsequence of the second. Otherwise, it returns False.A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.