
    # The number of n-digit numbers is 10**n.
    # But we have subtracted the number of n-digit numbers that do not start or end with 1.
    # These numbers are 10**n - 2*9**n because 9**n numbers do not start with 1 and 9**n numbers do not end with 1.
    # So the numbers that start or end with 1 are 10**n - 2*9**n.

    return 10**n - 2*9**n

print(starts_one_ends(2))
print(starts_one_ends(3))
print(starts_one_ends(4))
print(starts_one_ends(10))
<jupyter_output>
8
9
81
1017987131318606590
<jupyter_text>
Problem 3: Maximum Number of Divisors (10 points)Given an integer n, find the maximum number of divisors a number can have in an interval from 1 to n (both inclusive). Return the number that has the maximum number of divisors.
<jupyter_code>
