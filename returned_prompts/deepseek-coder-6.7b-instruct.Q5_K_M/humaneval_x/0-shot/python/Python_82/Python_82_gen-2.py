
    def prime_length(string):
        length = len(string)
        if length < 2:
            return False
        for i in range(2, int(length**0.5) + 1):
            if length % i == 0:
                return False
        return True

    print(prime_length('Hello'))  # True
    print(prime_length('abcdcba'))  # True
    print(prime_length('kittens'))  # True
    print(prime_length('orange'))  # False

The function `prime_length` works by first checking if the length of the string is less than 2. If it is, the function immediately returns False, because 0 and 1 are not prime numbers. 

Then, it checks if the length is divisible by any integer in the range from 2 to the square root of the length. The square root is used because a larger factor of the number would be a multiple of smaller factor that has already been checked.

If the length is divisible by any of these integers, the function returns False, because the length is not prime. If it is not divisible by any of these integers, the function returns True, because the length is prime.
<jupyter_output>
<empty_output>
<jupyter_text>
Task 2
<jupyter_code>
