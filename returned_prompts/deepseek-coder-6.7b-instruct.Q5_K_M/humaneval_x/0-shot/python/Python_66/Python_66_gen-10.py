
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())

print(digitSum("")) #=> 0
print(digitledigitSum("abAB")) #=> 131
print(digitSum("abcCd")) #=> 67
print(digitSum("helloE")) #=> 69
print(digitSum("woArBld")) #=> 131
print(digitSum("aAaaaXa")) #=> 153

Explanation:

The function `digitSum` takes a string `s` as input. It calculates the sum of the ASCII values of the uppercase characters in the string. This is done using the built-in function `sum`, which adds up the elements of an iterable.

The `ord` function is used to get the ASCII value of a character. The `isupper` method is used to filter out the uppercase characters.

The result is then returned by the function.

The `print` statements at the end are used to test the function with various inputs.
"""

# Task 2:

"""
