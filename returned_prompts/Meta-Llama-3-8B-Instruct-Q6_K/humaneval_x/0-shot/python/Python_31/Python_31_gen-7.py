def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
        


This function checks whether a given number is prime or not. It first checks if the number is less than or equal to 1, in which case it's not prime. Then it checks if the number is 2, which is the only even prime number. If the number is divisible by 2, it's not prime. If the number passes these checks, the function then checks divisibility from 3 up to the square root of the number, incrementing by 2 each time (since all primes are of the form 6k ± 1). If the number is divisible by any of these values, it's not prime. If it's not divisible by any of these values, it's prime.