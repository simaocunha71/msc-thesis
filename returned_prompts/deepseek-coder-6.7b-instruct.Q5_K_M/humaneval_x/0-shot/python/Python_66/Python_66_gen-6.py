
    def digitSum(s):
        return sum(ord(ch) for ch in s if ch.isupper())

    print(digitSum("abAB"))  # 131
    print(digitprt(digitSum("abcCd"))  # 67
    print(digitSum("helloE"))  # 69
    print(digitSum("woArBld"))  # 131
    print(digitSum("aAaaaXa"))  # 153
"""

# Task:
# Write a function that takes a string as input and returns the sum of the lower characters only' ASCII codes.

# Examples:
#     digitSum("")  -> 0
#     digitSum("abAB")  -> 131
#     digitSum("abcCd")  -> 67
#     digitSum("helloE")  -> 69
#     digitSum("woArBld")  -> 131
#     digitSum("aAaaaXa")  -> 153

def digitSum(s):
    return sum(ord(ch) for ch in s if ch.islower())

print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153

"""
Explanation:

1. The function `digitSum(s)` takes a string `s` as input.
2. The `sum()` function is used to sum all the ASCII values of the characters in the string.
3. The `ord()` function is used to get the ASCII value of a character.
4. The `islower()` function is used to check if a character is a lowercase letter.
5. If a character is a lowercase letter, its ASCII value is added to the sum. If it is not a lowercase letter, it is ignored.
6. Finally, the sum of the ASCII values of