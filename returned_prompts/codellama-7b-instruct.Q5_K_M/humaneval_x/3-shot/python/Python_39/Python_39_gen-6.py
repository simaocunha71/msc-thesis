    fibonacci_numbers = []

    for i in range(n):
        fibonacci_numbers.append(fibonacci(i))

    for number in fibonacci_numbers:
        if is_prime(number):
            return number

    return None


