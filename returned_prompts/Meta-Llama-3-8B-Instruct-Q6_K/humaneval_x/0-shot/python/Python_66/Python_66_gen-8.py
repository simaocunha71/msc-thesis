def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())  # Pythonic way

# Explanation:
# The function `digitSum` takes a string `s` as input.
# It uses a generator expression to iterate over each character `c` in the string `s`.
# The `ord` function is used to get the ASCII code of each character.
# The `if c.isupper()` condition is used to filter out the characters that are not upper case.
# The `sum` function is used to calculate the sum of the ASCII codes of the upper case characters.
# The function returns the sum of the ASCII codes of the upper case characters.

# Test cases:
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```



This function works by iterating over each character in the input string, and for each character, it checks if the character is an uppercase letter using the `isupper()` method. If the character is an uppercase letter, it calculates the ASCII code of the character using the `ord()` function and adds it to the sum. Finally, it returns the sum of the ASCII codes of the uppercase letters.

The function is tested with different input strings, and the output is checked to ensure that it matches the expected result. The function passes all the test cases, indicating that it is working correctly.