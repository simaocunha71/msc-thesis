"""
First, we need to understand what an amicable number is.
Two numbers are said to be amicable if the sum of the proper divisors of each is equal to the other number.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore, sum is 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so, sum is 220. 
Hence, 220 and 284 are an amicable pair.

We need to find all such pairs and sum all numbers in each pair.

Here is a python function that does the task:

"""


def divisor_sum(n):
    div_sum = 1
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            if i * (n // i) == n:
                div_sum = div_sum + i + n//i
            else:
                div_sum = div_sum + i
            i += 1
    return div_sum

def amicable_numbers_sum(limit):
    result = 0
    arr = [0] * (limit+1)
    for i in range(1, limit+1):
        arr[i] = divisor_sum(i)
    for i in range(1, limit+1):
        if arr[i] != i and arr[i] <= limit and arr[arr[i]] == i:
            result += i
    return result

print(amicable_numbers_sum(999))

assert amicable_numbers_sum(999)==504

"""
This program firstly calculates the sum of divisors for each number up to the limit. Then it checks each number to see if it's part of an amicable pair. If it is, it adds the number to the result. The function returns the sum of all amicable numbers.