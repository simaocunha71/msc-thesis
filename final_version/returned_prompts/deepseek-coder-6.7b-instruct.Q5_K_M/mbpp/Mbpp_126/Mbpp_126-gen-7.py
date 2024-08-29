
def sum_divisors(n1, n2):
    divisors = []
    for i in range(1, min(n1, n2)+1):
        if n1 % i == 0 and n2 % i == 0:
            divisors.append(i)
    return sum(divisors)

print(sum_divisors(10, 15))  # 6

Explanation:

We define a function sum_divisors that takes two numbers n1 and n2. We initialize a list divisors that will store all the common divisors of n1 and n2. We then loop from 1 to the minimum of n1 and n2, inclusive. If i is a divisor of both n1 and n2 (i.e., n1 and n2 mod i is 0), we append i to divisors. Finally, we return the sum of all elements in divisors.

The time complexity of this function is O(min(n1, n2)) because we are looping from 1 to min(n1, n2). The space complexity is also O(min(n1, n2)) because in the worst case, all divisors of n1 and n2 could be stored in divisors.

In the example, the common divisors of 10 and 15 are 1, 5, and 10. Their sum is 16. However, since 10 is not a divisor of 15, we only consider 1 and 5. Their sum is 6.
"""

# Q2

