    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    max_prime = max([x for x in lst if is_prime(x)])
    return sum(int(digit) for digit in str(max_prime))  # Convert to string and sum digits
    # This is a simple way to sum digits of a number. You could also convert to list and use sum() function
    # But in this case, using sum() with generator expression (int(digit) for digit in str(max_prime)) is more efficient
    # as it creates a generator and only creates the list of digits when the sum() function actually needs them.  #


