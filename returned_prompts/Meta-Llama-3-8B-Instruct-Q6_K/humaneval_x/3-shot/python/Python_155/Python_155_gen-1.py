    def is_even(x):
        return x % 2 == 0

    even_count = sum(is_even(int(digit)) for digit in str(abs(num)))
    odd_count = len(str(abs(num))) - even_count
    return (even_count, odd_count)  # return a tuple with even and odd count


