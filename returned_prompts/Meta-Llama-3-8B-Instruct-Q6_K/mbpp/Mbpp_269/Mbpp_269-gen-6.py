def ascii_value(char):
    return ord(char)
# ord is a built-in function in python that returns the ASCII value of a character. It works with both lowercase and uppercase letters, and also with other characters. 

# The unit test provided in the problem ensures that the function works correctly for uppercase letters. For example, the test `assert ascii_value('A')==65` checks that the ASCII value of 'A' is 65, which is true.

# You can use the function like this:
# print(ascii_value('A')) # Output: 65
# print(ascii_value('a')) # Output: 97
# print(ascii_value('1')) # Output: 49
# print(ascii_value('!')) # Output: 33
# and so on for any character.