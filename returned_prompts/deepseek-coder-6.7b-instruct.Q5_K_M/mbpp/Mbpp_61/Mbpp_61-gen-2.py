
def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        sum_digits = 0
        for j in range(i, len(s)):
            sum_digits += int(s[j])
            if sum_digits == j - i + 1:
                count += 1
    return count

print(count_Substrings('112112'))  # 6

"""
Explanation:

The function count_Substrings takes a string s as input and initializes a count to 0.

Then it iterates over the string. For each character in the string, it sets sum_digits to 0 and starts a nested loop that iterates from the current character to the end of the string.

In the nested loop, it adds the integer value of the current character to sum_digits and checks if sum_digits is equal to the difference between the current index j and the initial index i plus 1.

If this condition is true, it increments count.

Finally, it returns count.

This code counts the number of substrings in the input string where the sum of the digits of the substring is equal to the length of the substring.
"""
<jupyter_output>
6
<jupyter_text>
