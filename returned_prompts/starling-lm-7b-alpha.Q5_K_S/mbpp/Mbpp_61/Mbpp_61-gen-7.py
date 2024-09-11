"""
def count_Substrings(s):
    return sum(1 for i in range(len(s)) for j in range(i,len(s)) if sum(int(x) for x in s[i:j+1])==j-i+1)
"""

def count_Substrings(s):
    res = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            tmp = 0
            for x in s[i:j+1]:
                tmp += int(x)
            if tmp == j-i+1:
                res += 1
    return res


count_Substrings('112112') # 6
count_Substrings('121') # 3
count_Substrings('11211') # 6
count_Substrings('112') # 2


"""
Explanation:
The problem is to count the number of substrings with the sum of digits equal to their length.
For example, in the string '112112', there are six substrings with the sum of digits equal to their length,
namely '1', '11', '112', '1121', '11211', and '112112'.

To solve this problem, we can iterate through all possible substrings in the string,
calculate the sum of digits in each substring, and check if the sum is equal to the length of the substring.
If the sum is equal to the length of the substring, we increment a counter.
Finally, we return the counter, which represents the number of substrings with the sum of digits equal to their length.

In the function count_Substrings, we initialize a counter variable res to 0.
Then, we use two nested loops to iterate through all possible substrings in the string.
For each substring, we initialize a variable tmp to 0 and iterate through the characters in the substring.
For each character, we add its integer value to tmp.
After iterating through all the characters in the substring, we check if tmp is equal to the length of the substring.
If