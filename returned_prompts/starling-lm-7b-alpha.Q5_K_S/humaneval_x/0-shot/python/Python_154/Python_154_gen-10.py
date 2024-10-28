
def cycpattern_check(a , b):
    return b in a or (b[:-1] in a and len(b) > 1)

# def cycpattern_check(a , b):
#     for i in range(len(b)):
#         if b[i:] + b[:i] in a:
#             return True
#     return False

# def cycpattern_check(a , b):
#     for i in range(len(b)):
#         if b[i:] + b[:i] in a:
#             return True
#     return False


cycpattern_check("whassup","psus")
```
    
Here are some notes on this problem:

For each character in the second string (b), we check if the string formed by concatenating the substring starting from the current index (i) till the end of the second string (b) with the substring starting from the start of the second string (b) till the index (i) (i.e., b[i:] + b[:i]) is a substring in the first string (a).

Since the index (i) can be anywhere between 0 and length of the second string (b), it means that for each character in the second string (b), we check if the substring formed as described above is in the first string (a).

If the substring formed as described above is a substring in the first string (a) for any index (i), we return True, else False.

This solution has a time complexity of O(n^2), where n is the length of the second string (b).

Here are some more notes on this problem:

To solve this problem, we can check if the second word or any of its rotations is a substring in the first word.

To check if the second word or any of its rotations is a substring in the first word, we can concatenate the substring starting from the current index (i) till the end of the second word (b) with the substring starting from the start of the second word (b) till the index (i) (i.e., b[i:] + b[:i]) and check if this concatenated string is a