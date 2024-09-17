```
def occurance_substring(string, substring):
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            return substring, pos, pos+len(substring)
        start += 1
    return None
```
This function iterates over the input string and uses the find method to locate the substring. If the substring is found, it returns the substring, its position in the string, and its length. If the substring is not found, it returns None. The unit test provided ensures that the function works correctly for the given input. 

For example, `occurance_substring('python programming, python language','python')` returns `('python', 0, 6)`, which indicates that the substring 'python' is found at position 0 and its length is 6. 

If the substring is not found, the function returns None, as shown in the unit test. For instance, `occurance_substring('java', 'python')` returns None. 

The function is case-sensitive and considers both the order and the position of the characters in the substring. It also considers the order and position of characters in the string. 

The time complexity of this function is O(n*m), where n is the length of the input string and m is the length of the substring. This is because in the worst-case scenario, the function has to iterate over the entire string and for each iteration, it has to check the entire substring. The space complexity is O(1), as it uses a constant amount of space to store the variables. 