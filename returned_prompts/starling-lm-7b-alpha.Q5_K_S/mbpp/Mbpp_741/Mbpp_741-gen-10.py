"""
def all_Characters_Same(word):
    if len(word) == 1:
        return True
    if len(word) > 1:
        for i in range(len(word)-1):
            if word[i] != word[i+1]:
                return False
        return True

print(all_Characters_Same("python"))
"""

def all_Characters_Same(word):
    if len(word) == 1:
        return True
    if len(word) > 1:
        for i in range(len(word)-1):
            if word[i] != word[i+1]:
                return False
        return True

print(all_Characters_Same("python"))


# Python Program to check if all characters of a string are same or not

def all_Characters_Same(word):
    if len(word) == 1:
        return True
    if len(word) > 1:
        for i in range(len(word)-1):
            if word[i] != word[i+1]:
                return False
        return True

print(all_Characters_Same("python"))

"""
In this Python program, we define a function called all_Characters_Same that takes a string as an argument. This function checks if all the characters in the string are the same or not.

To do this, the function first checks if the length of the string is 1. If it is, then all the characters in the string are the same by default, so the function returns True.

If the length of the string is greater than 1, the function enters a for loop. This loop iterates over the range of indices from 0 to len(word)-1. Inside the loop, it compares the character at index i with the character at index i+1. If they are not the same, the function immediately returns False, indicating that all the characters in the string are not the same.

If the loop completes without returning False, it means that all the characters in the string are the same, so the function returns True.

Finally, we call the function with the string "python" and print the result, which will be False.
"""