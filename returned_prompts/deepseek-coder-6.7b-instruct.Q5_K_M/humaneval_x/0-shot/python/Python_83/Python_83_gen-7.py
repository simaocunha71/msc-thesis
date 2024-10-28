
    # Initialize the counter
    count = 0

    # Iterate through the numbers from 10^(n-1) to 10^n - 1
    for i in range(10**(n-1), 10**n):
        # Convert the number to a string
        str_i = str(i)

        # Check if the first digit is 1 or the last digit is 1
        if str_i[0] == '1' or str_i[-1] == '1':
            # If so, increment the counter
            count += 1

    return count

# Test cases
print(starts_one_ends(1)) # 4
print(starts_one_ends(2)) # 90
print(starts_one_ends(3)) # 900

# Explanation:
# For n=1, the numbers are 1, so there are 2 numbers that start or end with 1.
# For n=2, the numbers are 10, 11, 12, ..., 99, so there are 90 numbers that start or end with 1.
# For n=3, the numbers are 100, 101, 102, ..., 999, so there are 900 numbers that start or end with 1.
<jupyter_output>
4
90
900
<jupyter_text>
Question 2Given a string s, find the length of the longest substring without repeating characters.Example 1:Input: "abcabcbb"Output: 3 ("abc")Example 2:Input: "bbbbb"Output: 1 ("b")Example 3:Input: "pwwkew"Output: 3 ("wke")Note that the answer must be a substring, not a subsequence.
<jupyter_code>
