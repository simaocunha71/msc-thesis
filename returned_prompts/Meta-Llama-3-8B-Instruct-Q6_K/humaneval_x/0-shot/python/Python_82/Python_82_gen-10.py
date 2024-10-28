```
def prime_length(string):
    length = len(string)
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return is_prime(length)
``` 

The function `prime_length` calculates the length of the input string and then checks if this length is a prime number using the helper function `is_prime`. The `is_prime` function checks if a number is prime by testing divisibility up to the square root of the number. If the number is divisible by any of these values, it is not prime and the function returns `False`. If the number is not divisible by any of these values, it is prime and the function returns `True`. The `prime_length` function then returns the result of the `is_prime` function for the length of the input string. 

The unit tests provided in the problem statement ensure that the function works correctly for the given examples. For example, `prime_length('Hello')` returns `True` because the length of the string 'Hello' is 5, which is a prime number. Similarly, `prime_length('abcdcba')` returns `True` because the length of the string 'abcdcba' is 7, which is also a prime number. On the other hand, `prime_length('orange')` returns `False` because the length of the string 'orange' is 6, which is not a prime number. 





Final Answer: The final answer is the provided function. I hope it is correct.