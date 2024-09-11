def occurance_substring(s, sub):
    result = []
    for i in range(len(s)):
        if s[i:i+len(sub)] == sub:
            result.append((sub, i, i+len(sub)-1))
    if result:
        return result[0]
    else:
        return None

print(occuarance_substring('python programming, python language', 'python'))





"""
The idea behind the function is to scan the string from left to right, and every time when it encounters the substring, it will append the substring, its start index and end index to the result list.
The time complexity of the function is O(n), where n is the length of the string, because for each character in the string, at most O(1) operations are needed.
"""

"""
This function will return None if there is no match, because if the result list is empty, it means that there is no match of the substring in the string.
"""
"""
The function will return the first match it found, because it appends the result to the result list every time when it encounters the substring, and there can be multiple matches in the string.
"""
"""
The function will return a tuple, containing the substring, its start index and end index in the string.
"""
"""
The function will return the position of the substring in the string, which is the start index of the substring.
"""
"""
The function will return the length of the substring in the string, which is the end index of the substring minus the start index of the substring plus 1.
"""



















"""
Here are some example of the function:

assert occurance_substring('python programming, python language', 'python') == ('python', 0, 6)
assert occurance_substring('hello world', 'world') == ('world', 7, 8)
assert occurance_substring('hello world', 'hello') == None
assert occurance_substring('hello world', 'h') == ('h', 0, 1)

"""

"""
This function uses the sliding window technique to find the occurrence and