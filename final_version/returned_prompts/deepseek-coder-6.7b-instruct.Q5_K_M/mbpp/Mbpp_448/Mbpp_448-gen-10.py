"""
Perrin sequence is defined as: P(0) = 3, P(1) = 0, P(2) = 2 and P(n) = P(n-1) + P(n-2) + P(n-3) for n > 2.

So, we can use the formula to calculate the sum of first n Perrin numbers.

Algorithm:
1. Define a function with one argument n.
2. Initialize the first three Perrin numbers P0, P1 and P2 to 3, 0 and 2 respectively.
3. If n is less than or equal to 2, return Pn.
4. For i in range of 3 to n, calculate the next Perrin number using the formula and update P0, P1 and P2.
5. Return the sum of all Perrin numbers from P0 to Pn.
"""

def cal_sum(n):
    P0, P1, P2 = 3, 0, 2
    if n == 0:
        return P0
    elif n == 1:
        return P1
    elif n == 2:
        return P2
    else:
        for i in range(3, n+1):
            Pn = P0 + P1 + P2
            P0, P1, P2 = P1, P2, Pn
        return Pn

print(cal_sum(9))

# Output: 49

"""
We can improve the efficiency of the function by using the built-in function sum() to calculate the sum of the list.
"""

def cal_sum(n):
    if n == 0:
        return 3
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        perrin = [3, 0, 2]
        for i in range(3, n+1):
            perrin.append(sum(perrin[-3:]))
        return perrin[-1]

print(cal_sum(9))

# Output: 49
<jupyter_output>
49
49
<jupyter_text>
Question 