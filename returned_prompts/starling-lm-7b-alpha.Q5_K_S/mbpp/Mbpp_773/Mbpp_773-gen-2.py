
def occurance_substring(string, substring):
    if substring in string:
        return (substring, string.index(substring), string.index(substring)+len(substring))
    else:
        return None

# Driver program
print(occuarance_substring('python programming, python language', 'python'))




"""
The time complexity of the above program is O(n) because in the worst case the function index() can be called n times, where n is the length of the string.
"""

"""
The above program will not work correctly for the following two cases:
1. If there are multiple substrings with the same value, only the first occurrence will be returned.
2. If the string contains multiple occurrences of the substring, only the first occurrence will be returned.
"""

def occurance_substring(string, substring):
    start = 0
    while True:
        index = string.find(substring, start)
        if index == -1:
            return None
        yield (substring, index, index + len(substring))
        start = index + 1

# Driver program
for result in occurance_substring('python programming, python language', 'python'):
    print(result)

"""
The time complexity of this program is O(n) because in the worst case the function find() can be called n times, where n is the length of the string.
"""

"""
The above program will return all the occurrences of the substring. It will also return the start and end index of each occurrence of the substring in the string.
"""

"""
The above program will not work correctly if the substring is not found in the string. In that case, it will raise an IndexError. To handle this situation, you can add an if-else statement to check if the index is -1 and return None if it is.
"""



"""
The above program will also not work correctly if the substring is not found at the beginning of the string. In that case, it will raise an IndexError. To handle this situation, you can add an if-else statement to check if the index is -1 and return None if it is.
"""

"""
The above program will also not work correctly if