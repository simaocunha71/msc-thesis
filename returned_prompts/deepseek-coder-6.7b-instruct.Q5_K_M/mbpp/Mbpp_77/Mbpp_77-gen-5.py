def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

print(gcd(12, 15))

#Q7
"""
Write a python function to find the least common multiple (LCM) of two numbers.
assert lcm(5, 7) == 35
"""
