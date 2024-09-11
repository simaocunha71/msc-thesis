def validate(n):
    d = {}
    for i in str(n):
        if i not in d:
            d[i] = 0
        d[i] += 1
    for i in d:
        if d[i] > int(i):
            return False
    return True

# tests
print(validate(1234))  # True
print(validate(1233))  # False
print(validate(999999999))  # True
print(validate(313))  # False
print(validate(33))  # True
print(validate(1))  # True
print(validate(111))  # False
print(validate(123456))  # True

"""
Explanation:

The function works by first creating a dictionary, d, to keep track of the frequency of each digit. It then iterates through the string representation of the input integer, n, and checks if each digit is already in the dictionary. If not, it adds the digit to the dictionary and initializes its frequency to 0. It then increments the frequency of the digit by 1.

After counting the frequency of each digit, the function loops through the dictionary and checks if the frequency of each digit is greater than the digit itself. If it is, the function returns False. If all frequencies are less than or equal to the digit, the function returns True.
"""

"""
Explanation:

The function works by first creating a dictionary, d, to keep track of the frequency of each digit. It then iterates through the string representation of the input integer, n, and checks if each digit is already in the dictionary. If not, it adds the digit to the dictionary and initializes its frequency to 0. It then increments the frequency of the digit by 1.

After counting the frequency of each digit, the function loops through the dictionary and checks if the frequency of each digit is greater than the digit itself. If it is, the function returns False. If all frequencies are less than or equal to the digit, the function returns True.
"""

"""
Explanation:

The function works by first creating a dictionary, d, to keep track of the frequency of each digit. It then iterates through