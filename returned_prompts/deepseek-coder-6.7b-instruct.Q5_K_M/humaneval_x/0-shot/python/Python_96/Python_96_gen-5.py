
def count_up_to(n):
    primes = []
    for num in range(2, n):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

print(count_up_to(5))  # [2, 3]
print(count_up_to(11))  # [2, 3, 5, 7]
print(count_up_to(0))  # []
print(count_up_to(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(1))  # []
print(count_up_to(18))  # [2, 3, 5, 7, 11, 13, 17]

In this function, we iterate over all numbers from 2 up to n. For each number, we check if it is a prime number by iterating over all numbers from 2 to the current number. If the current number is not divisible by any of these numbers, it is a prime number and we append it to the list of prime numbers.

The time complexity of this function is O(n^2) because for each number from 2 to n, we are checking if it is divisible by any number from 2 to the current number. This is not an efficient solution and it's better to use the Sieve of Eratosthenes algorithm which has a time complexity of O(n log log n).

This function will return an empty list if the input is 1 or 0 because there are no prime numbers less than 2.

Note: This solution assumes that the input is a non-negative integer. If the input can be a float or a string, additional error checking should be added.


'''

# Solution 2

'''
def count_up_to(n):
    primes = []
    for num in range(2, n):
        if num > 1:
            for i in range(2, int(num