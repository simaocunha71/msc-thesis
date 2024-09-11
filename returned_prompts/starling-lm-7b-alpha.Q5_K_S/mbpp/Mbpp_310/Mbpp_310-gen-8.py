def string_to_tuple(string):
    return tuple(string)


# Another way:
# def string_to_tuple(string):
#     return tuple(list(string))


if __name__ == '__main__':
    print(string_to_tuple("python 3.0"))  # Output: ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')




"""
In addition to the function above, we can use the list method to convert a string into a tuple.
However, the time complexity of this method is O(n), where n is the length of the string, because it first converts the string to a list and then converts the list to a tuple.
"""


"""
In addition to the above two methods, Python also provides a built-in method called tuple() to convert a string to a tuple, which has a time complexity of O(n).
"""

"""
We can also convert a string to a tuple by using the built-in map() function to convert each character to a tuple, and then convert the resulting list to a tuple.
However, this approach also has a time complexity of O(n).
"""

# Python's tuple() function has a time complexity of O(n).
# def string_to_tuple(string):
#     return tuple(string)


# Using the built-in map() function has a time complexity of O(n).
# def string_to_tuple(string):
#     return tuple(map(str, string))


# Another way: Using the built-in map() function to convert each character to a tuple, and then convert the resulting list to a tuple. This approach also has a time complexity of O(n).
# def string_to_tuple(string):
#     return tuple(map(lambda x: (x,), string))


# Another way: Using the built-in map() function to convert each character to a tuple, and then convert the resulting list to a tuple. This approach also has a time complexity of O(n).
# def string_to_tuple(string):
#     return tuple(map(str, string))


"""
The time complexity of these three methods is