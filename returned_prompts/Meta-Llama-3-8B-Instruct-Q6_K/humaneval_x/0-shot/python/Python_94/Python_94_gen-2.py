def skjkasdkd(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    max_prime = 0
    for num in lst:
        if is_prime(num) and num > max_prime:
            max_prime = num

    return sum(int(digit) for digit in str(max_prime))
# This function first defines a helper function is_prime to check if a number is prime. Then it iterates over the list, checks if each number is prime and if it's greater than the current max prime, it updates the max prime. Finally, it returns the sum of the digits of the max prime.