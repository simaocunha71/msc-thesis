
def count_up_to(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    primes = []
    for i in range(n):
        if is_prime(i):
            primes.append(i)
    return primes

print(count_up_to(5))  # [2, 3]
print(count_up_to(11))  # [2, 3, 5, 7]
print(count_up_to(0))  # []
print(count_up_to(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(1))  # []
print(count_up_to(18))  # [2, 3, 5, 7, 11, 13, 17]

# this function works by iterating through the numbers from 0 to n-1, 
# checking if each one is prime, and if it is, appending it to the primes list.
# the is_prime helper function checks if a number is prime by checking if any number from 2 to num-1 divides it evenly.
# if any number divides it evenly, it is not prime, so the function returns False. if no numbers divide it evenly, it is prime, so the function returns True.
<jupyter_output>
[2, 3]
[2, 3, 5, 7]
[]
[2, 3, 5, 7, 11, 13, 17, 19]
[]
[2, 3, 5, 7, 11, 13, 17]
<jupyter_text>
Question 2
<jupyter_code>
