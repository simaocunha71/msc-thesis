
def digitSum(s):
    # Initialize a variable to store the sum
    sum = 0
    # Iterate over each character in the string
    for c in s:
        # Check if the character is an uppercase alphabet
        if c.isupper():
            # If it is, add its ASCII code to the sum
            sum += ord(c)
    return sum

# Test the function
print(digitSum(""))   # 0
print(digitSum("abAB"))   # 131
print(digitSum("abcCd"))   # 67
print(digitSum("helloE"))   # 69
print(digitSum("woArBld"))   # 131
print(digitSum("aAaaaXa"))   # 153

# The above code works, but can be optimized

def digitSum(s):
    # Initialize a variable to store the sum
    sum = 0
    # Iterate over each character in the string
    for c in s:
        # Check if the character is an uppercase alphabet
        if c.isupper():
            # If it is, add its ASCII code to the sum
            sum += ord(c)
    return sum

# Test the function
print(digitSum(""))   # 0
print(digitSum("abAB"))   # 131
print(digitSum("abcCd"))   # 67
print(digitSum("helloE"))   # 69
print(digitSum("woArBld"))   # 131
print(digitSum("aAaaaXa"))   # 153

# The above code works, but can be optimized

def digitSum(s):
    # Initialize a variable to store the sum
    sum = 0
    # Iterate over each character in the string
    for c in s:
        # Check if the character is an uppercase alphabet
        if c.isupper():
            # If it is, add its ASCII code to the sum
            sum += ord(c)
    return sum

# Test the function
print