
def is_polite(n):
    # Checks if the number is divisible by 3, 4, and 6
    if n % 3 == 0 and n % 4 == 0 and n % 6 == 0:
        return n
    else:
        # If not, increment the number and check again
        return is_polite(n + 1)


