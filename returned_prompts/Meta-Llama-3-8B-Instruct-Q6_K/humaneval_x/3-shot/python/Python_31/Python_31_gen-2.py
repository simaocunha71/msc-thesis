    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
# This function checks if a number is prime by testing divisibility up to the square root of the number. It first handles the edge cases where the number is less than or equal to 1, or less than or equal to 3. Then it checks if the number is divisible by 2 or 3. If not, it starts checking divisibility from 5, incrementing by 6 each time (since we can skip even numbers after 2 and numbers divisible by 3 after 3). If the number is not divisible by any of these, it is prime.