def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())  # Pythonic way
    # return sum(ord(c) for c in s if c.isupper())  # Alternative way
    # sum = 0
    # for c in s:
    #     if c.isupper():
    #         sum += ord(c)
    # return sum


# Test cases
print(digitSum(""))  # Expected output: 0
print(digitSum("abAB"))  # Expected output: 131
print(digitSum("abcCd"))  # Expected output: 67
print(digitSum("helloE"))  # Expected output: 69
print(digitSum("woArBld"))  # Expected output: 131
print(digitSum("aAaaaXa"))  # Expected output: 153

# Explanation:
# The function digitSum takes a string as input and returns the sum of the ASCII codes of the upper case characters in the string.
# The isupper() function is used to check if a character is an uppercase letter.
# The ord() function is used to get the ASCII code of a character.
# The sum() function is used to calculate the sum of the ASCII codes.
# The function returns the sum of the ASCII codes of the upper case characters in the string.