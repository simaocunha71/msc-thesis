
def check_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print(check_integer("python"))  # False
print(check_integer("123"))  # True

# Another way to solve this problem is to use the isdigit() string method:
def check_integer_2(s):
    return s.isdigit()

print(check_integer_2("python"))  # False
print(check_integer_2("123"))  # True

# Python's isdigit() method returns True if all characters in the string are digits, otherwise False. 
# This method is a simple way to check if a string can be converted to an integer.

# The try and except block is used to catch exceptions. In this case, if the string cannot be converted to an integer (which is the exception), the function will return False. 
# If the string can be converted to an integer without an exception, the function will return True.
<jupyter_output>
False
True
False
True
<jupyter_text>
