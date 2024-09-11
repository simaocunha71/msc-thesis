def all_Characters_Same(input_string):
    '''This function takes a string as an argument and returns True if all the characters in the string are the same and False if not.'''
    if len(set(input_string)) == 1:
        return True
    else:
        return False

# test case
print(all_Characters_Same("python"))  # prints False














"""
Time complexity: O(n)
Space complexity: O(1)
"""

def all_Characters_Same(input_string):
    '''This function takes a string as an argument and returns True if all the characters in the string are the same and False if not.'''
    if len(set(input_string)) == 1:
        return True
    else:
        return False

# test case
print(all_Characters_Same("python"))  # prints False

"""
The time complexity of this function is O(n) because in the worst case, we need to iterate through all the characters in the string.
The space complexity of this function is O(1) because the worst-case scenario is when the set of unique characters in the string is of size 1, and in this case, the space complexity is O(1).
"""














"""
In the code above, we first convert the input string into a set of unique characters using the set() function. Then, we compare the length of the set with 1. If the length is 1, it means all the characters in the string are the same, and we return True. Otherwise, we return False.

The time complexity of this function is O(n), where n is the length of the input string. This is because we need to iterate through all the characters in the string to create the set of unique characters. The space complexity is O(1), as the worst-case scenario is when the set of unique characters in the string is of size 1, and in this case, the space complexity is O(1).
"""














"""
In the code above, we first convert the input string into a set of unique characters using the set() function