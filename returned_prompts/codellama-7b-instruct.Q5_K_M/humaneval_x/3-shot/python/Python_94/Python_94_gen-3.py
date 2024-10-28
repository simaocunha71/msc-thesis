    largest_prime = 0
    largest_prime_sum = 0

    for i in range(len(lst)):
        if is_prime(lst[i]):
            if lst[i] > largest_prime:
                largest_prime = lst[i]
                largest_prime_sum = sum(str(largest_prime))

    return largest_prime_sum


