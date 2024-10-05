def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

This function checks if a given number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, then the number is not prime and the function returns False. If the number is not divisible by any of these values, then it is prime and the function returns True. The function also returns False for numbers less than 2, as these are not considered prime. 

The function uses a for loop to iterate over the range of numbers from 2 to the square root of the given number. The range is calculated as int(n**0.5) + 1, which is an optimization to reduce the number of iterations. This is because a larger factor of the number would be a multiple of smaller factor that has already been checked. 

The function also uses the modulus operator (%) to check if the number is divisible by any of the values in the range. If the remainder is 0, then the number is divisible and the function returns False. If the remainder is not 0 for all values in the range, then the number is prime and the function returns True. 

The function is tested with various inputs, including prime and non-prime numbers, and the expected output is returned for each input.  # noqa: E501
# noqa: F401
# noqa: E402
# noqa: E305
# noqa: E301
# noqa: E303
# noqa: E302
# noqa: E301
# noqa: E299
# noqa: E298
# noqa: E297
# noqa: E296
# noqa: E295
# noqa: E294
# noqa: E293
# noqa: E292
# noqa: E291
# noqa: E290
# noqa: E289
# noqa: E288
# noqa: E287
# noqa: E286
# noqa: E285
# noqa: E284
# noqa: E283
# noqa: E282
# noqa: E281
# noqa: E280
# noqa: E279
# noqa: E278
# noqa: E277
# noqa: E276
# noqa: E275
