    # Find largest prime number in list
    largest_prime = max(lst)

    # Convert number to string
    largest_prime = str(largest_prime)

    # Add up digits of number
    digits = 0

    for c in largest_prime:
        digits += int(c)

    return digits


