
def multiply(a, b):
    return (abs(a) % 10) * (abs(b) % 10)

# Test cases
print(multiply(148, 412))  # should return 16
print(multiply(19, 28))  # should return 72
print(multiply(2020, 1851))  # should return 0
print(multiply(14, -15))  # should return 20


# This solution works by taking the modulus of each number by 10 (which gives the unit digit) and multiplying them together.
# The abs function is used to ensure we get the unit digit of both numbers, regardless of their sign.
<jupyter_output>
16
72
0
20
<jupyter_text>
Explanation:This problem is asking us to find the product of the last digit of two given numbers. We can achieve this by taking the modulus of each number by 10 (which gives the last digit). Then, we multiply these last digits together. Note that we use the absolute value of the numbers in case they are negative. This is because negative numbers do not have a unit digit, and we should consider the positive equivalent instead.  Problem 3: Largest and Smallest SumWrite a function that takes a list of integers and returns the sum of the largest and smallest integers in the list.Assume that the list will always contain at least one integer. Examples:largest_smallest_sum([1, 2, 3, 4, 5]) should return 6 (which is 1 + 5 = 6)largest_smallest_sum([10, 11, 12, 13, 14]) should return 24 (which is 10 + 14 = 24)largest_smallest_sum([-10, -11, -12, -13, -14]) should return -24 (which is -10 + -14 = -24)
<jupyter_code>
