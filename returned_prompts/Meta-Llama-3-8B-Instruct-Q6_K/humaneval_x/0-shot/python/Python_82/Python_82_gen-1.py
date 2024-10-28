def prime_length(string):
    length = len(string)
    if length <= 1:
        return False
    for i in range(2, int(length ** 0.5) + 1):
        if length % i == 0:
            return False
    return True
# test cases
print(prime_length('Hello')) # True
print(prime_length('abcdcba')) # True
print(prime_length('kittens')) # True
print(prime_length('orange')) # False

This function works by first calculating the length of the input string. It then checks if this length is less than or equal to 1, in which case it returns False (since 0 and 1 are not prime numbers). 

It then iterates over all numbers from 2 to the square root of the length, and checks if the length is divisible by any of these numbers. If it is, the function returns False, since the length is not a prime number. 

If the function doesn't find any divisors, it returns True, since the length is a prime number. 

This function correctly identifies the lengths of the test strings as prime or not prime.  For example, the length of 'Hello' is 5, which is a prime number, so the function returns True.  The length of 'orange' is 6, which is not a prime number, so the function returns False.  The lengths of 'abcdcba' and 'kittens' are both 7 and 7 is also a prime number, so the function returns True for these strings. 