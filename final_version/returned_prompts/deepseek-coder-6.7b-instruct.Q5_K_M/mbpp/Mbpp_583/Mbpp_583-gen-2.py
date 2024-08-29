def catalan_number(n):
    if n<=1:
        return 1
    res = 0
    for i in range(n):
        res += catalan_number(i) * catalan_number(n-i-1)
    return res

print(catalan_number(10))

# Time complexity: O(n^2)
# Space complexity: O(n)

"""
Explanation:
The Catalan numbers are a sequence of positive integers that appear in many counting problems in combinatorics. They can be given by the formula:

C(n) = (2n choose n) / (n+1)

Here, (2n choose n) is the binomial coefficient.

In this program, we calculate the nth Catalan number using a recursive method. For every number 'n', we calculate the Catalan numbers for all numbers 'i' from 0 to 'n-1' and multiply them together. We add these products to a variable 'res' which is returned as the nth Catalan number.

The time complexity of this program is O(n^2) because the function calls itself for every number from 0 to n-1, and it takes O(n) time to calculate the binomial coefficient. The space complexity is O(n) because of the call stack when we use a recursive approach.
"""
<jupyter_output>
16796
<jupyter_text>
