"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""

def sum_of_common_divisor(n1, n2):
   if n1 < n2:
      return sum_of_common_divisor(n2, n1)    # this line is the heart of our algorithm
   else:
       return 0                                # n1 == n2, just do nothing here
for num in range(40):
   print("sum of common divisors for %d and %d" % (num+1, num+2))
print('done')