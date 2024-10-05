
def is_multiply_prime(a):
    # a is less than 100
    if a > 100:
        return False

    # check if a is a prime number
    if a == 2 or a == 3 or a == 5:
        return True

    # check if a can be divided by 2 or 3 or 5
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False

    return True

    # Alternative:
    def is_multiply_prime(a):
        if a > 100:
            return False

        if a == 2 or a == 3 or a == 5:
            return True

        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False

        return True

        # Alternative:
        def is_multiply_prime(a):
            if a > 100 or a == 1:
                return False

            for i in range(2, int(a ** 0.5) + 1):
                if a % i == 0:
                    return False

            return True

            # Alternative:
            def is_multiply_prime(a):
                if a > 100 or a == 1:
                    return False

                for i in range(2, int(a ** 0.5) + 1):
                    if a % i == 0:
                        return False

                return True

                # Alternative:
                def is_multiply_prime(a):
                    if a > 100 or a == 1:
                        return False

                    for i in range(2, int(a ** 0.5) + 1):
                        if a % i == 0:
                            return False

                    return True

                    # Alternative:
                    def is_multiply_prime(a):
                        if a > 100 or a == 