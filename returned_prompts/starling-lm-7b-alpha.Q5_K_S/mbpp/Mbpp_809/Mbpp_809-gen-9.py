def check_smaller(t1, t2):
    for i in range(len(t1)):
        if t1[i] > t2[i]:
            return False
    return True

# Test
print(check_smaller((1, 2, 3), (2, 3, 4)))  # False
print(check_smaller((1, 2, 1), (2, 3, 4)))  # True





"""
Given a string, find the length of the longest substring, which has all unique characters.

Explanation:
The length of the longest substring is 5. For example, the substring "abcde" is a valid substring.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The longest substring with all distinct characters is "abc".

Example 2:
Input: "bbbbbb"
Output: 1
Explanation: The longest substring with all distinct characters is "b".

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The unique substring is "wke".

"""

def lengthOfLongestSubstring(s):
    result = 0
    last_seen = {}
    for i in range(len(s)):
        if s[i] in last_seen:
            start = last_seen[s[i]] + 1
            result = max(result, i - start + 1)
        else:
            result = max(result, i - start + 1)
        last_seen[s[i]] = i
    return result

# Test
print(lengthOfLongestSubstring("abcabcbb"))  # 3
print(lengthOfLongestSubstring("bbbbbb"))   # 1
print(lengthOfLongestSubstring("pwwkew"))   # 3



"""
Given an array of integers, find the maximum sum of a contiguous subarray.

Explanation:
The largest sum is 7, which is the sum of 1, 2, 3, 4, 5, 6,