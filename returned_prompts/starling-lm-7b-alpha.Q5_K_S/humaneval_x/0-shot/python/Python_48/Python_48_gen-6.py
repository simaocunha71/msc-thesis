def is_palindrome(text: str) -> bool:
    return text == text[::-1]
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """


# Python3 program to check if a string is palindrome or not

# Function to check if a string is palindrome or not
def checkPalindrome(str):

    # Run length of string
    length = len(str)

    # Loop to check if string is palindrome or not
    for i in range(0, length/2):
        # Check if characters at positions i and length - i - 1 are same or not
        if str[i] != str[length - i - 1]:
            return False

    # If above loop completes without returning false, then
    # the string is a palindrome and we return true
    return True


# Driver program to test above function
str = "geeksforgeeks"
if (checkPalindrome(str)):
    print("Yes")
else:
    print("No")


def palindrome(string):
    # Initialize left index and right index
    left = 0
    right = len(string) - 1

    # While there are characters to compare
    while right >= left:

        # If there is a mismatch
        if string[left] != string[right]:
            return False

        # Increment left index and decrement right index
        left += 1
        right -= 1

    # If we reach here, then the string is a palindrome
    return True


# Driver program to test above function
print(palindrome("racecar"))  # True
print(palindrome("abacus"))  # False


# Python3 program to check if a string is palindrome or not

# Function to check if a string is palindrome or not
def checkPalindrome(str):

