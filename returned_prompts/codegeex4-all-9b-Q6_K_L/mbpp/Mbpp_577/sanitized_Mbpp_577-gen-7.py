def last_Digit_Factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    
    # Recursive case: n! = n * (n-1)!
    last_digit = (n % 10) * last_Digit_Factorial(n - 1) % 10
    
    return last_digit