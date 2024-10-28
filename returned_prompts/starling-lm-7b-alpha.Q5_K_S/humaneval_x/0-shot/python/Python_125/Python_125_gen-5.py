
def split_words(txt):
    txt = txt.split(' ')
    if len(txt) == 0:
        return len(txt)
    if ',' in txt:
        return txt.split(',')
    return sum(1 for c in txt if ord(c) % 2 == 1)

# Alternate Solution
def split_words(txt):
    txt = txt.split(' ')
    if len(txt) == 0:
        return len(txt)
    if ',' in txt:
        return txt.split(',')
    return len([c for c in txt if ord(c) % 2 == 1])

# Alternate Solution
def split_words(txt):
    return (len([c for c in txt if ord(c) % 2 == 1]) if ',' not in txt else txt.split(',')) if txt else len(txt)



# Code Explanation
# The function split_words takes a string as an input. It first checks if the string is empty. If it is, it returns the length of the string.
# If the string contains a comma, it splits the string on the comma and returns the result.
# If neither of the above conditions are met, it checks if the string has any lowercase letters with odd order in the alphabet. It does this by using a list comprehension to iterate through the string and checking the ordinal value of each character. If the ordinal value modulus 2 is equal to 1, it adds the character to the list. Finally, it returns the length of the list.

# Alternate Solution 1:
# This alternate solution uses a similar approach to the original solution, but instead of using the sum function to count the number of odd characters, it uses a list comprehension to count the number of odd characters.

# Alternate Solution 2:
# This alternate solution uses a ternary operator to simplify the conditional logic. It checks if the string is empty or contains a comma, and if so, it returns the result of the corresponding branch. If neither condition is met, it returns the length of the list of odd characters.

# Time Complexity: O(n), where n is the length of the input string. This is