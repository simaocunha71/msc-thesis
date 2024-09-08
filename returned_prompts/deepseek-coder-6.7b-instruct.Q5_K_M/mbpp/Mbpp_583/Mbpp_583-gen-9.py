def catalan_number(n):
    if n<=1:
        return 1
    else:
        catalan = [0 for _ in range(n+1)]
        catalan[0] = 1
        catalan[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i-j-1]
        return catalan[n]

print(catalan_number(10)) #16796

"""
Explanation:
The function first handles the base cases where n is less than or equal to 1. If n is 0 or 1, it returns 1 since the 0th and 1st catalan numbers are 1.

If n is greater than 1, we start by initializing a list named catalan with n+1 zeros. We then set the first two elements of the list to 1.

We then start a loop from 2 to n (both inclusive). For every number i in this range, we start another loop from 0 to i-1 (both inclusive). For every j in this inner loop, we update the i-th element of the catalan list by adding the product of the j-th element of the catalan list and the (i-j-1)-th element of the catalan list to it.

Finally, we return the nth element of the catalan list as the nth catalan number.
"""
<jupyter_output>
16796
<jupyter_text>
**Problem 3**Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.**Example**For example, if s = "babad", the output should be "bab". Note that "aba" is also a valid answer.**Solution**
<jupyter_code>
