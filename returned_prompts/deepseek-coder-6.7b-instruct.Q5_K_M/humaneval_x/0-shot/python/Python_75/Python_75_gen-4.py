
def is_multiply_prime(a):
    count = 0
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        while a % i == 0:
            a = a / i
            count += 1
            if a % i != 0:
                break
    if a > 1:
        count += 1
    return count == 3

print(is_multiply_prime(30))  # True

The function works by iteratively dividing the given number by each integer from 2 to the square root of the number. If the number is divisible, it is divided and the count of factors is incremented. If the number is not divisible, the loop increments to the next integer. If the count of factors is equal to 3 at the end of the loop, the function returns True, otherwise it returns False.

The reason we only need to check divisors up to the square root of the number is because a larger factor of the number would be a multiple of smaller factor that has already been checked.

Also, we don't need to check for even numbers as all even numbers will not be prime.

The function returns False if the number is less than 2 because there are no prime numbers less than 2.

The function returns False if the count of factors is not equal to 3 because a number can only be the product of 3 prime numbers if it has exactly 3 distinct prime factors.

This function has a time complexity of O(sqrt(n)) because it iterates over a range of numbers up to the square root of the given number.

This function has a space complexity of O(1) because it only uses a constant amount of extra space to store the count of factors and the given number.

This function is correct because it correctly determines whether a number can be expressed as the product of exactly 3 prime numbers.

This function is efficient because it uses a simple loop to check for factors, which runs in linear time.

This function is useful because it can be used to solve a variety of problems where prime factorization is needed, such as cryptography, number theory, and computer science.

This function is simple because it uses a simple loop to check for factors and a simple if statement