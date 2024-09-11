def divisor(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

# Testing the function
print(divisor(15))  # Should print 4




"""
In the above code, we define a function called divisor that takes an integer n as a parameter. We initialize a variable called count to 0 to keep track of the number of divisors.
We then use a for loop to iterate through all the numbers from 1 to n (inclusive). For each number i, we check if it is a divisor of n by checking if the remainder of the division of n by i is 0.
If the condition is true, it means that i is a divisor of n, so we increment the count variable by 1. Finally, we return the count variable, which will hold the total number of divisors of n.
"""



"""
To test the function, we can call it with a sample input, such as 15, and print the result. The function should return 4, as the divisors of 15 are 1, 3, 5, and 15, so the count should be 4.
"""



"""
In this specific case, we can also use the built-in function reduce() from the functools module to simplify the code. The reduce() function applies a given function to the elements of an iterable (in this case, a range of numbers) in a cumulative way to reduce it to a single result.
Here's how we can use reduce() to find the number of divisors of a given integer:
"""



"""
from functools import reduce

def divisor(n):
    return reduce(lambda x, y: x + (n % y == 0), range(1, n + 1), 0)

print(divisor(15))  # Should print 4
"""



"""
In this version of the function, we use a lambda function as the first argument to reduce(). The lambda function takes two arguments, x and y, and returns x + 1 if y is a divisor of n (i.e