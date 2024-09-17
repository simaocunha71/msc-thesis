```
def amicable_numbers_sum(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def sum_of_divisors(num):
        total = 0
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                total += i
                if i != num // i:
                    total += num // i
        return total

    def is_amicable(num1, num2):
        if num1 == num2:
            return False
        return sum_of_divisors(num1) == num2 and sum_of_divisors(num2) == num1

    total_sum = 0
    for i in range(2, n + 1):
        if not is_prime(i):
            for j in range(i * 2, n + 1):
                if is_amicable(i, j):
                    total_sum += i + j
    return total_sum
```


This solution calculates the sum of all amicable numbers from 1 to a specified number. It first defines three helper functions: `is_prime` to check if a number is prime, `sum_of_divisors` to calculate the sum of the divisors of a number, and `is_amicable` to check if two numbers are amicable.

Then it initializes a variable `total_sum` to zero and iterates over all numbers from 2 to the specified number. For each number, it checks if the number is not prime. If it's not prime, it iterates over all numbers from the square of the current number to the specified number, and checks if the current number and the other number are amicable. If they are, it adds their sum to `total_sum`.

Finally, it returns `total_sum`. The unit test `assert amicable_numbers_sum(999)==504` ensures that the function works correctly.