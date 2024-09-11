"""
The function `find_substring` receives a list of strings and a string as arguments and returns a boolean.
It checks if the string is present in any of the strings of the list and returns True if it is and False if not.
"""

def find_substring(list_strings, string):
    for i in list_strings:
        if string in i:
            return True
    return False


if __name__=="__main__":
    assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
    assert find_substring(["red", "black", "white", "green", "orange"],"purple")==False
    print("All tests passed")

#created by Jigar Trivedi





















"""
A substring is a contiguous sequence of characters within a string. The length of a string is the number of characters in the string.
"""
"""
In computer science, a string is traditionally considered as an ordered sequence of zero or more characters (or, more generally, elements). The individual elements or symbols in the string are referred to as characters or string elements. The string is a data structure that is used to store a sequence of characters.
"""
"""
A string is a sequence of characters. It is one of the fundamental data types in programming. In Python, strings are immutable sequences of characters. They are declared using single or double quotation marks.
"""
"""
A string is a sequence of characters. Strings are immutable, meaning that they cannot be changed after they are created. This means that you cannot change the contents of a string after it has been created.
"""
"""
In Python, a string is a sequence of characters. Strings are immutable, meaning that you cannot change the contents of a string after it has been created.
"""
"""
A string is a sequence of zero or more characters. It is an immutable, one-dimensional array of characters.
"""
"""
A string is a sequence of characters. It is one of the fundamental data types in programming. In Python, strings are immutable sequences of characters. They are declared using single or double quotation marks.
"""
"""
A string is a