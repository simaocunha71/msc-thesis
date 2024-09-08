
def sum_Of_product(n):
    from math import comb
    sum = 0
    for i in range(1, n):
        sum += comb(n, i) * comb(n, i+1)
    return sum

print(sum_Of_product(3)) #15

"""
Explanation:

Here, we use the combination function from the math module to calculate binomial coefficients. 
The function comb(n, i) gives the number of ways to choose i items from n items without repetition and without order.

For n=3, the possible pairs are (1,2), (1,3), and (2,3).
The product of consecutive binomial co-efficients for these pairs are 3*2=6, 3*1=3 and 2*1=2.
So the sum is 6+3+2=11.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
**Question 2** **Question**Given a string s, find the length of the longest substring without repeating characters.**Example**Input: s = "abcabcbb"Output: 3Explanation: The longest substring is "abc" with length 3. **Solution**Here is a Python solution using sliding window technique.
<jupyter_code>
def length_of_longest_substring(s):
    char_set = set()
    left = 0
    result = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        result = max(result, right - left + 1)

    return result

print(length_of_longest_substring("abcabcbb"))  # Output: 3
<jupyter_output>
3
<jupyter_text>
**Question 3** **Question**You are given an array of integers. Return an array of the same length, where the element at each index i is the product of all the numbers in the original array except the one at i.