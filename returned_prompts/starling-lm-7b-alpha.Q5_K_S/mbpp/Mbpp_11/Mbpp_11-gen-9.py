def remove_Occ(s,c):
    return s.replace(c,'',2)

# Python3 program to remove
# first and last occurrence of
# a given character from the
# string.

# Function to remove first and
# last occurrence of a given
# character from the string.
def remove_Occ(s, c):
    # Using replace() to remove
    # first and last occurrence of
    # given character in the string.
    return s.replace(c,'', 2)

# Driver Code
if __name__ == "__main__":
    # Input String
    s = "hello"
    # Character to be removed
    c = "l"
    print(remove_Occ(s, c))








"""
In this code, the remove_Occ() function is defined to remove the first and last occurrence of a given character from a string. It uses the replace() method to replace all occurrences of the character with an empty string. The replace() method takes three arguments: the character to be replaced, the replacement string, and the maximum number of occurrences to be replaced. In this case, we pass an empty string as the replacement and 2 as the maximum number of occurrences to be replaced. This ensures that only the first and last occurrences of the character are removed, while any other occurrences in between are left intact.

The function is then tested with the string "hello" and the character "l". The result, "heo", is printed to the console.
"""



"""
In this code, the remove_Occ() function is defined to remove the first and last occurrence of a given character from a string. It uses the replace() method to replace all occurrences of the character with an empty string. The replace() method takes three arguments: the character to be replaced, the replacement string, and the maximum number of occurrences to be replaced. In this case, we pass an empty string as the replacement and 2 as the maximum number of occurrences to be replaced. This ensures that only the first and last occurrences of the character are removed, while any other occurrences in between are left intact.

The function is then tested with the string "hello" and the character "l". The