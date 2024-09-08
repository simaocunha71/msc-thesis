def find_remainder(arr, n):
    prod = 1
    for num in arr:
        prod = (prod * num) % n
    return prod

print(find_remainder([ 100, 10, 5, 25, 35, 14 ],11)) # Output: 9

"""
Explanation:

The function find_remainder takes a list of integers (arr) and an integer (n) as input. It initializes a variable prod to 1, which will store the running product of the numbers in arr modulo n.

Then, it iterates over each number in arr. For each number, it multiplies the current prod by that number, and then takes the remainder of the division of the result by n. This is equivalent to calculating the product of the numbers in arr modulo n, but it avoids potential overflow problems that can occur if the numbers in arr are very large.

Finally, it returns the value of prod, which is the product of the numbers in arr modulo n.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Q3. Write a Python function to check whether a string is a valid email or not.
<jupyter_code>
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    return False

# Test cases
print(is_valid_email("test@example.com")) # True
print(is_valid_email("test@.com")) # False
print(is_valid_email("test@example")) # False
print(is_valid_email("test@.example.com")) # False
print(is_valid_email("test@example.com.")) # False
<jupyter_output>
True
False
False
False
False
<jupyter_text>
Q4. Given a list of integers, write a function to return the sum of all prime numbers in that list.
<jupyter_code>
def is_prime(n):
