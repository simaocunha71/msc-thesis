"""
We can solve this problem by using the definition of amicable numbers.

An amicable number is a number that is equal to the sum of its proper divisors excluding the number itself.

For example, let's take number 220, its proper divisors are 1,2,4,5,10,11,20,22,44,55 and 110, of which the sum is 284. If we add those to 220, we get 566 which is not the original number. This is an example of an amicable pair.

We can solve this problem by:
1. Creating a function to calculate the sum of proper divisors of a number.
2. Using a loop to go through all numbers from 1 to the specified number.
3. Checking if the sum of the proper divisors of a number equals to the number, if not, then checking if the sum of the proper divisors of the sum equals to the original number.
4. If they are equal, then the number is an amicable number.
5. Finally, sum all the amicable numbers.

Here is the Python code to do this:
"""

def proper_divisors_sum(n):
    divisors_sum = 0
    for i in range(1,n):
        if n%i == 0:
            divisors_sum += i
    return divisors_sum

def amicable_numbers_sum(n):
    amicable_numbers_sum = 0
    for i in range(1,n):
        if proper_divisors_sum(proper_divisors_sum(i)) == i and proper_divisors_sum(i) != i:
            amicable_numbers_sum += i
    return amicable_numbers_sum

print(amicable_numbers_sum(999))  # output: 504

"""
In this code, the function `proper_divisors_sum(n)` calculates the sum of the proper divisors of a number `n`. The function `amicable_numbers_sum(