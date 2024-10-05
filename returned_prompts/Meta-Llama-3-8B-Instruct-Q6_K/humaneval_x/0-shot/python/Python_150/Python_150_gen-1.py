def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(x_or_y(7, 34, 12))
print(x_or_y(15, 8, 5))



Output:
34
5

Explanation:
In this code, we first define the function x_or_y which takes three parameters, n, x, and y. This function checks if the number n is a prime number using the helper function is_prime. If n is a prime number, it returns the value of x, otherwise it returns the value of y.

The helper function is_prime checks if the number is less than 2, in which case it's not prime. Then it checks for divisibility from 2 to the square root of the number. If the number is divisible by any of these, it's not prime. If it's not divisible by any of these, it's a prime number.

Finally, we call the function x_or_y with the arguments 7, 34, and 12, and then with the arguments 15, 8, and 5. The output is 34 and 5, which are the expected results.