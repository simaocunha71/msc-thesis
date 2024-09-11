def tup_string(tup):
    return ''.join(tup)


# Driver code
print(tup_string(('e', 'x', 'a', 'm', 'p', 'l', 'e')))

# This code is contributed by Anant Agarwal.


"""

The above program uses a built-in Python function called join() to convert a tuple to a string. The join() function is a string method that concatenates all the strings in a tuple with a specified string (separator) in between. The separator is optional. If you don't provide a separator, it concatenates all the strings without any separator in between.

"""



# Time Complexity: O(n), where n is the number of elements in the tuple
# Space Complexity: O(1), the extra space used is constant















"""

def tup_string(tup):
    result = ""
    for i in tup:
        result += i
    return result


# Driver code
print(tup_string(('e', 'x', 'a', 'm', 'p', 'l', 'e')))

# This code is contributed by Anant Agarwal.

"""

In the above program, we manually concatenate all the strings in the tuple to form a string. This method is less efficient and less readable than the previous method.
"""












































































































































































