
def check_if_last_char_is_a_letter(txt):
    # check if string is empty
    if len(txt) == 0:
        return False
    # get the last character of the string
    last_char = txt[-1]
    # check if the last character is an alphabetical character
    if last_char.isalpha():
        # check if the last character is the last word
        if not txt[-1].isalnum():
            return True
    return False

check_if_last_char_is_a_letter("apple pie")  # False
check_if_last_char_is_a_letter("apple pi e")  # True
check_if_last_char_is_a_letter("apple pi e ")  # False
check_if_last_char_is_a_letter("")  # False



# Python3 program to find if all
# characters in a string are present
# in another string

# Function to check if all characters
# of first string are present in the
# second string
def check_all_present(str1, str2):

    # Iterate over the first string
    # and check if all characters
    # of the first string are present
    # in the second string
    for i in str1:

        # If any character is not present
        # return false
        if i not in str2:
            return False

    # If all characters are present
    # return true
    return True


# Driver program
str1 = "abc"
str2 = "acb"
if (check_all_present(str1, str2)):
    print("Yes")
else:
    print("No")



# Python3 program to count the
# frequency of each element
# in an array

from collections import Counter

# Function to count the frequency
# of each element in an array
def count_frequency(arr, n):

    # Create an empty dictionary
    freq = {}

    # Traverse through all characters
    # of the string
    for i in range(n):

        # If the character is already
        # present in the dictionary
