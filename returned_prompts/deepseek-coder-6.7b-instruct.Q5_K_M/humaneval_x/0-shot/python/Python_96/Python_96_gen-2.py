
def count_up_to(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes


print(count_up_to(5))  # [2, 3]
print(count_up_to(11))  # [2, 3, 5, 7]
print(count_up_to(0))  # []
print(count_up_to(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(1))  # []
print(count_up_to(18))  # [2, 3, 5, 7, 11, 13, 17]

# Time complexity: O(n^2)
# Space complexity: O(n)

# The is_prime function has a time complexity of O(n) and is called n times in the main function, so the total time complexity is O(n^2).
# The space complexity is O(n) as we are storing the prime numbers in a list.

# The problem with this code is that it checks for prime numbers for numbers less than n, while we only care about prime numbers that are less than n. 
# So we need to change the range of numbers in the for loop in the main function to be from 2 to n.

def count_up_to(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes


print(count_up_to(5))  #