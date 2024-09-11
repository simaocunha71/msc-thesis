def sum_in_range(l, r):
    sum = 0
    for i in range(l, r + 1):
        if i % 2 != 0:
            sum += i
    return sum

# Test Case
assert sum_in_range(2, 5) == 8



"""
In this function, we start by initializing a variable sum to zero. We then loop through all the numbers between l and r (inclusive) using the range function. For each number, we check if it's odd by using the modulus operator (%). If the number is odd, we add it to the sum variable. Finally, we return the sum.
"""

"""
Test Case:

Here we are testing the function sum_in_range(2, 5) which should return 8. The function takes two arguments, l and r, representing the lower and upper bounds of the range. The function iterates through all the numbers between l and r (inclusive) and checks if each number is odd. If a number is odd, it is added to the sum. In this case, the odd numbers between 2 and 5 are 3, 5, and the sum of these numbers is indeed 8, so the test case passes.
"""

"""
Complexity Analysis:

The time complexity of this function is O(n) where n is the number of odd numbers between l and r (inclusive). In the worst case, all numbers between l and r (inclusive) are odd, so the function will need to check each number once.

The space complexity of this function is O(1) as we only use a single variable, sum, to store the result.
"""

"""
Alternative Solution:

An alternative solution to this problem is to use the formula for the sum of an arithmetic series, which is (n/2)(first_term + last_term). In this case, the first_term is the smallest odd number in the range (which can be calculated as (l + 1)/2) and the last_term is the largest odd number in the range (which can be calculated as (r - 1)/2). The total number of odd numbers in the range can be calculated as (r - l)/2 + 1. Using this formula, the function