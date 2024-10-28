    if n % 2 == 0:
        if n >= 8:
            if n == 8:
                return True
            else:
                return is_equal_to_sum_even(n - 4)
        else:
            return False
    else:
        return False


