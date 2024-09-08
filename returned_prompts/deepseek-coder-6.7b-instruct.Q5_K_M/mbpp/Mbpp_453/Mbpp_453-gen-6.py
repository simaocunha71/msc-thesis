"""
A function to calculate the sum of even factors of a number can be written as follows:

1. First, we initialize a variable named 'sum' to 0.
2. Then we run a loop from 1 to the square root of the given number.
3. In the loop, we check if the number is divisible by the current number.
4. If it is, then the current number and the number/current number are factors of the given number.
5. We then check if the current number is even.
6. If it is, then we add the current number to the sum.
7. After the loop ends, we return the sum.

Here is the Python code for the above steps:
"""

import math

def sumofFactors(n):
    sum = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i % 2 == 0:
                sum += i
            if (n/i) % 2 == 0:
                sum += n//i
    return sum

print(sumofFactors(18))

# Output:
# 26

# Explanation:
# The even factors of 18 are 2, 4, 6, and 18. The sum of these factors is 26.

"""
This function works by iterating through all numbers from 1 to the square root of the given number (inclusive), checking if each number is a factor of the given number. If it is, and if the number is even, we add it to the sum. We also check if the number n/i (where i is the current number) is even and add it to the sum. This ensures that we don't count any factors twice.
"""


"""
Here, the time complexity is O(sqrt(n)) because we're looping through all the numbers up to the square root of n. The space complexity is O(1) because we're using a constant amount of space to store the sum and the numbers.
"""

# Tests:

assert sumofFactors(18) == 26
assert sumofFactors(24) == 46
assert sumofFactors(2