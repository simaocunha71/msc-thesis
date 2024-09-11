from math import sqrt
def prime_num(x):
    if x<2:
        return False
    if x==2:
        return True
    if x%2==0:
        return False
    if x==3:
        return True
    if x%3==0:
        return False
    d=5
    while d<=sqrt(x):
        if x%d==0:
            return False
        if x%(d+2)==0:
            return False
        d+=6
    return True


# Created by: Arlester Guevara
# Date: 10/23/2018
# This program checks if an inputted number is prime

"""
This program first checks if the number is less than 2 because if it is, it is not prime. It then checks if the
number is equal to 2 because if it is, it is prime. It then checks if the number is divisible by 2 because if it is, it is not prime. It then checks if the number is equal to 3 because if it is, it is prime. It then checks if the number is divisible by 3 because if it is, it is not prime. It then initializes d with 5 and begins a while loop that ends when d is greater than the square root of the inputted number. Inside the loop, it checks if the number is divisible by d and d+2 because if it is, it is not prime. It increments d by 6 in each iteration because all prime numbers greater than 3 are of the form 6k ± 1 where k is an integer. The function then returns true if all checks pass, meaning the number is prime, and false if any of the checks fail, meaning the number is not prime.
"""

# Test
print(prime_num(13))
"""
This line of code tests the function by passing in the number 13 and asserting that the output should be True. This is because 13 is a prime number, meaning it only has two factors, 1 and itself.
"""

# Time Complexity: O(sqrt(n))
# Space Complexity: O(1)

"""
The time complexity of this program is O(sqrt(n)) because the while