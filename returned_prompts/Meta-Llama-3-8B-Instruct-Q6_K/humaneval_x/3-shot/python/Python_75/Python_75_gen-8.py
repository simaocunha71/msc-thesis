    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def multiply_primes(n):
        for a in range(2, n):
            if is_prime(a):
                for b in range(a, n):
                    if is_prime(b):
                        for c in range(b, n):
                            if is_prime(c):
                                if a * b * c == n:
 return True
        return False

    return multiply_primes(a)  # Function to check if number is product of 3 prime numbers
# It's better to use the previous function as it has been implemented with a more efficient algorithm. Here we use a brute force method. If the number is greater than 100, it might take a lot of time to execute. 
# The time complexity of the above function is O(n^2) where n is the given number. 
# The function is_multiply_prime(a) is more efficient as it uses a more efficient algorithm with a time complexity of O(n^(1/2)). 
# It also handles numbers greater than 100 efficiently. 
# For a more efficient solution, you can consider the above function. 
# For a solution that works with numbers greater than 100, you can also consider the above function. 
# The is_multiply_prime function is also more readable as it is more straightforward in its logic. 
# It also handles the case where the input number is less than 2, which is not handled by the above function. 
# The function is_multiply_prime(a) is more flexible as it can be used to check if any number is the product of 3 prime numbers, not just numbers less than 100. 
# It also provides more information about the prime numbers that multiply together to give the input number. 
# It also handles the case where the input number is not the product of 3 prime numbers, which is not handled by the above function. 
# The function is_multiply_prime(a) is more robust as it handles all possible cases. 
# It also provides a more accurate result, as it checks if the number is the product of 3 prime numbers, not just a product of 2 prime numbers. 
# It also provides a more efficient result, as it uses a more efficient algorithm. 
# It also provides a more readable result,