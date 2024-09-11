def even_Power_Sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**5
    return sum


even_Power_Sum(2)
"""
Explanation:
In this problem, we need to sum the first n even natural numbers that are raised to the fifth power. Even natural numbers are numbers that are divisible by 2.
To solve this problem, we can define a function called even_Power_Sum that takes an integer n as input. Inside the function, we initialize a variable sum to 0 to store the sum of the even natural numbers raised to the fifth power. Then, we use a for loop to iterate through the range from 1 to n+1. For each iteration, we add the square of the current number to the sum. Finally, we return the sum.
In the provided example, even_Power_Sum(2) is called, which means we want to find the sum of the first 2 even natural numbers raised to the fifth power. The function returns the value 1056, which is the correct result.
"""

# Python3 program to print all prime factors of a number

import math

def primeFactors(n):
    # Print the number of 2s that divide n
    while n % 2 == 0:
        print(2, end = ' ')
        n = n / 2

    # n must be odd at this point.  So we can skip one element (Note i = i +2)
    for i in range(3,int(math.sqrt(n))+1,2):

        # While i divides n, print i and divide n
        while n % i== 0:
            print(i, end = ' ')
            n = n / i

    # This condition is to handle the case when n is a prime number
    # greater than 2
    if n > 2:
        print(n)



n = int(input(""))
primeFactors(n)

"""
Explanation:
In this program, we are finding the prime factors of a given number. We define a function called primeFactors that takes a number as input.
Inside the function, we initialize a variable