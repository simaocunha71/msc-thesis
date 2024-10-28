
def cycpattern_check(a, b):
    for i in range(len(b)):
        if b in a:
            return True
        b = b[-1:] + b[:-1]
    return False

print(cycpattern_check("abcd","abd")) #=> False
print(cycpattern_check("hello","ell")) #=> True
print(cycpattern_check("whassup","psus")) #=> False
print(cycpattern_check("abab","baa")) #=> True
print(cycpattern_check("efef","eeff")) #=> False
print(cycpattern_check("himenss","simen")) #=> True


# This solution works by iterating over the length of the second word and rotating it. It then checks if this new string is a substring of the first word. If it is, the function returns True. If it never finds a match, it returns False.

# The time complexity of this solution is O(n*m) where n is the length of the first word and m is the length of the second word.
# The space complexity of this solution is O(1) because it only uses a fixed amount of space.
<jupyter_output>
False
True
False
True
False
True
<jupyter_text>
**Problem 5**:Write a function that will solve the following problem:You are given a list of integers and a number. You need to return the index of the first occurrence of that number in the list. If the number is not found, return -1.```pythonfind_first_occurrence([5, 4, 1, 2, 1, 3, 1, 4, 5, 1], 1) ➞ 2find_first_occurrence([5, 5, 5, 5, 5, 5, 5], 5) ➞ 0find_first_occurrence([], 1) ➞ -1```
<jupyter_code>
def find_first_occurrence(lst, num):
    try:
        return lst.index(num)
    except ValueError: