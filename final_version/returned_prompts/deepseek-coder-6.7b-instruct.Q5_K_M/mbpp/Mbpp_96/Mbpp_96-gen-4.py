def divisor(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

print(divisor(15))  # 4

# Other solution

def divisor(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if n / i == i:
                count += 1
            else:
                count += 2
    return count

print(divisor(15))  # 4

"""
The function works by iterating through all numbers from 1 to n, and incrementing a counter each time it finds a number that evenly divides n (i.e., n % i == 0).

The optimized version uses the fact that a divisor of n must be less than or equal to the square root of n, and it only needs to iterate through those numbers. If the square root of n is an integer, we count it as a divisor of n.
"""
<jupyter_output>
4
4
<jupyter_text>
**Question 2**
<jupyter_code>
