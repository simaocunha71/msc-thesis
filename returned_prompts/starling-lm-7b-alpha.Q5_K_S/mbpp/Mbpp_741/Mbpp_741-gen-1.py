def all_Characters_Same(s):
    return len(set(s)) == 1

# Testing the function
assert all_Characters_Same("python") == False
assert all_Characters_Same("python") == False
assert all_Characters_Same("a") == True

# Multiple Test Cases
test_cases = [
    ("python", False),
    ("a", True),
    ("pppp", True),
    ("abcd", False),
]

for s, expected in test_cases:
    assert all_Characters_Same(s) == expected, f"{s!r} -> {expected!r}"

print("All test cases passed.")


"""
Time Complexity: O(n), where n is the length of string s.
Space Complexity: O(n), where n is the length of string s.
"""


"""
Explanation:
In the given problem, we need to check whether all the characters in the string are the same or not. To solve this problem, we can create a set of characters from the string and check whether the length of the set is equal to 1 or not. If the length of the set is equal to 1, it means all the characters are the same, otherwise not.
The time complexity of the above approach is O(n), where n is the length of the string. This is because we are creating a set of characters from the string, which takes O(n) time.

The space complexity of the approach is also O(n), as the set of characters takes O(n) space.
"""


"""
The Python function to check whether all the characters are same or not is implemented as follows:

1. The function all_Characters_Same takes a string s as input and returns a boolean value.
2. Inside the function, we create a set of characters from the string s using the built-in set() function. This takes O(n) time, where n is the length of the string.
3. We then check whether the length of the set is equal to 1 using the len() function. This also takes O(n) time.
4. If the length of the set is equal to 1, we return True, indicating that all the characters are the same