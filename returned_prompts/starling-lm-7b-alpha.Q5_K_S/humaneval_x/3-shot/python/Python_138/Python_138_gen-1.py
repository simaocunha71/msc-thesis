    def is_even(n):
        return n % 2 == 0

    def is_sum_of_4_positive_even(n):
        for i in range(2, n+1, 2):
            if is_even(i) and is_even(n - i):
                return True
        return False

    return is_sum_of_4_positive_even(n)


