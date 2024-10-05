def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
    
# Test cases
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153

# Explanation
The function `digitSum` takes a string `s` as input and returns the sum of the ASCII codes of the upper case characters in the string.
The `ord` function is used to get the ASCII value of a character, and `isupper` is used to check if a character is an uppercase letter. The `sum` function is used to calculate the sum of the ASCII values.
In the test cases, the function is tested with different inputs and the expected output is printed. The function works correctly for all the test cases. 





Output:
0
131
67
69
131
153

Explanation:
The output of the function is the sum of the ASCII values of the uppercase characters in the input string. The function works correctly for all the test cases.