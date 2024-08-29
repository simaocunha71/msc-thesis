def sum_common_divisors(m, n):
    def common_divisors(x):
        return [i for i in range(1, x + 1) if x % i == 0]
    return sum(set(common_divisors(m)).intersection(common_divisors(n)))

print(sum_common_divisors(10, 15))  # 6

"""
Explanation:
This function works by first defining another function, common_divisors, which finds all divisors of a given number. 
It does this by iterating over all numbers from 1 to the given number (inclusive), and checking if the given number is 
divisible by the current number (i.e., if the remainder when the given number is divided by the current number is 0). 
If the current number is a divisor, it's added to a list. The function then returns this list of divisors.

After defining common_divisors, the main function sum_common_divisors finds the common divisors of m and n by calling 
common_divisors on each of them, and then finding their intersection (i.e., the common elements in the two lists).

Finally, it returns the sum of these common divisors.
"""

# Solution 2

def sum_common_divisors(m, n):
    def common_divisors(x):
        return set(i for i in range(1, x + 1) if x % i == 0)
    return sum(common_divisors(m).intersection(common_divisors(n)))

print(sum_common_divisors(10, 15))  # 6

"""
Explanation:
This solution uses a generator instead of a list for the common_divisors function. This makes it a bit more memory-efficient, 
especially for large inputs, because it doesn't need to store the entire list in memory. It also makes the code a bit cleaner, 
because it's a bit easier to read.

The rest of the code is the same as the first solution.
"""
<jupyter_output>
<empty_