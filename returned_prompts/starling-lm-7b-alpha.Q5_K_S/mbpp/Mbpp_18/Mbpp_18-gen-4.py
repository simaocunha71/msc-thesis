def remove_dirty_chars(string1, string2):
    """
    Write a function to remove characters from the first string which are present in the second string.
    """
    res = ''
    for char in string1:
        if char not in string2:
            res += char
    return res

if __name__ == '__main__':
    print(remove_dirty_chars("probasscurve", "pros"))
# This code is contributed by Saurabh Singh
"""

"""

# Python3 program to remove all
# characters from a string
# which are present in the other

# Function to remove all characters
# from a string which are present
# in the other string
def remove_chars(str1, str2):

    # Iterate over all characters of
    # string1
    for i in range(len(str1)):

        # If current character is present
        # in string2
        if str1[i] in str2:

            # Shift all characters after
            # current character by one
            # to the left
            str1 = str1[0:i] + \
                   str1[i + 1:len(str1)]

    return str1

# Driver code
if __name__ == '__main__':
    str1 = "probasscurve"
    str2 = "pros"

    print(remove_chars(str1, str2))

"""

# Python3 program to remove all
# characters from a string
# which are present in the other

# Function to remove all characters
# from a string which are present
# in the other string
def remove_chars(str1, str2):

    # Iterate over all characters of
    # string1
    for i in range(len(str1)):

        # If current character is present
        # in string2
        if str1[i] in str2:

            # Shift all characters after
            # current character by one
            # to the left
            str1 = str1[0:i] + \
                   str1[i + 1:len(str1)]

    return str1

