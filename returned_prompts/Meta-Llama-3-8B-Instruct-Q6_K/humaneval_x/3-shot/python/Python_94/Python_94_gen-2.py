    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    max_prime = max([i for i in lst if is_prime(i)])
    return sum(int(digit) for digit in str(max_prime))  # str(max_prime) to convert to string and then iterate over each character (digit) and convert back to int
# or
    return sum(map(int, str(max([i for i in lst if is_prime(i)])))
# or
    return sum(int(digit) for digit in str(max(i for i in lst if is_prime(i))))  # use a generator expression instead of a list comprehension
# or
    return sum(map(int, str(max(i for i in lst if is_prime(i)))))  # use a generator expression instead of a list comprehension and map function
# or
    max_prime = max([i for i in lst if is_prime(i)])
    return sum(int(c) for c in str(max_prime))  # str(max_prime) to convert to string and then iterate over each character (digit) and convert back to int
# or
    return sum(int(c) for c in str(max([i for i in lst if is_prime(i)])))  # use a generator expression instead of a list comprehension
# or
    max_prime = max([i for i in lst if is_prime(i)])
    return sum(map(int, str(max_prime)))  # str(max_prime) to convert to string and then iterate over each character (digit) and convert back to int
# or
    return sum(map(int, str(max(i for i in lst if is_prime(i)))))  # use a generator expression instead of a list comprehension and map function
# or
    return sum(int(digit) for digit in str(max([i for i in lst if is_prime(i)])))  # str(max_prime) to convert to string and then iterate over each character (digit) and convert back to int
# or
    return sum(int(c) for c in str(max([i for i in lst if is_prime(i)])))  # str(max_prime) to convert to string and then iterate over each character (digit) and convert back to int
# or
    return sum(map(int, str(max([i for i in lst if