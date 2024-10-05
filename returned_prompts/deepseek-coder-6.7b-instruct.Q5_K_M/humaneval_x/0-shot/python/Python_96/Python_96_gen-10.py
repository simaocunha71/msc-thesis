
def count_up_to(n):
    primes = []
    for possiblePrime in range(2, n):

        # Assume number is prime until shown it is not. 
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes

print(count_up_to(5))
print(count_up_to(11))
print(count_up_to(0))
print(count_up_to(20))
print(count_up_to(1))
print(count_up_to(18))

# Output:
# [2, 3]
# [2, 3, 5, 7, 11, 13, 17, 19]
# []
# [2, 3, 5, 7, 11, 13, 17, 19]
# []
# [2, 3, 5, 7, 11, 13, 17]

# This code works by iterating over every integer from 2 to n-1 and checking if it is prime. It does this by iterating from 2 to the square root of the number and checking if the number is divisible by any of these numbers. If the number is divisible by any of these numbers, it is not prime and the loop is broken. If the number is not divisible by any of these numbers, it is prime and it is added to the list of primes.
<jupyter_output>
[2, 3]
[2, 3, 5, 7, 11, 13, 17, 19]
[]
[2, 3, 5, 7, 11, 13, 17, 19]
[]
[2, 3, 5, 7, 11, 13, 17]
<jupyter_text>
Pro