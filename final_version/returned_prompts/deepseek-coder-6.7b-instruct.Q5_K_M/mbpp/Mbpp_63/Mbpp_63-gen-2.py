def max_difference(lst):
    return max(max(pair) - min(pair) for pair in lst)

print(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]))

"""
The function works by iterating over each pair in the list. For each pair, it finds the maximum and minimum value, and subtracts the minimum from the maximum. It then finds the maximum of all these differences.
"""
<jupyter_output>
7
<jupyter_text>
Problem 2: Find the Longest Palindrome in a StringGiven a string, find the longest palindrome in it. For example, in the string "abdbaz", the longest palindrome is "abdba".The function should be able to handle lower case letters and numbers. For example, in the string "a2b3c4c3b2a1", the longest palindrome is "a2b3c4c3b2a".The function should return the longest palindrome found in the string. If no palindrome is found, it should return an empty string.
<jupyter_code>
def longest_palindrome(s):
    # Initialize the longest palindrome to be an empty string
    longest_palindrome = ""
    # Iterate over each possible starting point of a substring in s
    for i in range(len(s)):
        # Iterate over each possible ending point of a substring in s
        for j in range(i+1, len(s)+1):
            # Get the substring from s from index i to j
            substring = s[i:j]
            # Check if the substring is a palindrome
            if substring == substring[::-1]:
                # Check if the substring is longer than the current longest palindrome
                if len(substring) > len(longest_palindrome):
                    # Update the longest palindrome
                    longest_palindrome = substring
    # Return the longest palindrome found
    return longest_palindrome

# Test the function
print(longest_palindrome("ab