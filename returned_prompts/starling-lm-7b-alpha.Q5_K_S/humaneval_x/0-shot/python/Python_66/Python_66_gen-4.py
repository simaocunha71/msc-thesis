
def digitSum(s):
    total = 0
    for char in s:
        if char.isupper():
            total += ord(char)
    return total

# Test
print(digitSum(""))       # 0
print(digitSum("abAB"))   # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE")) # 69
print(digitSum("woArBld"))# 131
print(digitSum("aAaaaXa"))# 153

# Explanation
# The function uses a for loop to iterate through all characters in the string.
# It checks if a character is upper case using the .isupper() method.
# If the character is upper case, it uses the .ord() method to get the ASCII code of the character and adds it to the total.
# Finally, the function returns the total sum of all upper case characters' ASCII codes.

# In Python, ASCII codes are represented by integers. For example, the ASCII code for 'A' is 65, for 'B' is 66, and so on.
# The .ord() method is used to convert a character to its ASCII code.

# The .isupper() method is a built-in Python method that checks if a character is upper case or not. It returns True if the character is upper case, and False otherwise.

# The .add() method is used to add a value to a variable. In this case, it is used to add the ASCII code of an upper case character to the total variable.

# The function returns the total sum of all upper case characters' ASCII codes, which is the result of the task.

# The test cases are provided to demonstrate the functionality of the function. Each test case shows an example input and the expected output.

# The explanation is written in a step-by-step manner to help understand the code and the logic behind it.

# The code uses a for loop to iterate through all characters in the string. It checks if a character is upper case using the .isupper() method. If the character is upper case, it uses the .ord