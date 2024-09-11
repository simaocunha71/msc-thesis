"""
def count_Substrings(s):
    return sum(1 for i in range(len(s)) for j in range(i + 1, len(s) + 1) if sum(int(k) for k in s[i:j]) == j - i)

def test_count_Substrings():
    assert count_Substrings('112112') == 6
    print("All tests passed.")

test_count_Substrings()
"""

def count_Substrings(s):
    return sum(1 for i in range(len(s)) for j in range(i + 1, len(s) + 1) if sum(int(k) for k in s[i:j]) == j - i)

def test_count_Substrings():
    assert count_Substrings('112112') == 6
    print("All tests passed.")

test_count_Substrings()

# Here is a detailed explanation:
# In the code, the function count_Substrings takes a string as input and returns the count of substrings with the sum of digits equal to their length.
# The function uses a nested loop to iterate through all possible substrings of the input string. The outer loop iterates through the starting index of the substring, and the inner loop iterates through the ending index.
# For each substring, the code calculates the sum of the digits using a generator expression and checks if the sum is equal to the length of the substring. If it is, the code increments the count by 1.
# Finally, the function returns the total count of substrings.
# In the test_count_Substrings function, the code asserts that the count_Substrings function correctly counts the number of substrings with the sum of digits equal to their length for the input string '112112', which should be 6.
# If the assertion is true, the code prints "All tests passed.". Otherwise, an error is raised.

# This code can be used to count the number of substrings with the sum of digits equal to their length for any input string.

# The time complexity of the code is O(n^3), where n is the length of the input string