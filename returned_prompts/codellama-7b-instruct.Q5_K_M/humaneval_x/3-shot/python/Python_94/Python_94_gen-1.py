    largest_prime = 0
    for i in lst:
        if is_prime(i):
            if largest_prime < i:
                largest_prime = i

    return sum(str(largest_prime))


