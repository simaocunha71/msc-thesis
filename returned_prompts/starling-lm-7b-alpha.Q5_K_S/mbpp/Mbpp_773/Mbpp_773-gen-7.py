def occurance_substring(s, w):
    # Your code here
    index = []
    for i in range(len(s)):
        if s[i:i+len(w)] == w:
            index.append((w, i, i+len(w)-1))
    if not index:
        return None
    else:
        return index


if __name__ == '__main__':
    print(occurance_substring('python programming, python language','python'))



"""
The above function is to find the occurrence and position of the substrings within a string.
We use a for loop to iterate through all possible starting positions of the substring in the given string.
If the substring matches the string starting from the current position, we append the substring, its starting position and ending position to the result list.
Finally, we return the result if there is a match, or None if there is no match.
"""


"""
In this test case, the function is called with the string 'python programming, python language' and the substring 'python'.
The function will return the tuple ('python', 0, 6), indicating that the substring 'python' is found at position 0 and its length is 6.
"""


"""
The time complexity of this function is O(n^2), where n is the length of the string.
This is because we need to compare the substring with the string for each possible starting position, which takes O(n) time in the worst case.
The space complexity is O(n), as we store the result in a list.
"""


"""
If you want to optimize the function, you can use the following approach:

Instead of checking the substring for every possible starting position, you can use KMP algorithm to find the occurrence and position of the substring within a string in linear time.
However, this requires implementing the KMP algorithm, which can be complex and time-consuming.

If you are not concerned about the time complexity, the above function should work fine for most cases.
"""




























"""
In the above code, we define a function