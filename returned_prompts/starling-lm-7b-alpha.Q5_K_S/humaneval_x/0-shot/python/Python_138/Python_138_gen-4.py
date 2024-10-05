    def is_even(num):
        return num % 2 == 0

    def is_sum_of_4_even(num):
        if num < 8:
            return False
        if is_even(num):
            return True
        else:
            if is_sum_of_4_even(num - 2) or is_sum_of_4_even(num - 4) or is_sum_of_4_even(num - 6) or is_sum_of_4_even(num - 8):
                return True
            else:
                return False

        return False

    return is_sum_of_4_even(n)


def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    def is_even(num):
        return num % 2 == 0

    def is_sum_of_4_even(num):
        if num < 8:
            return False
        if is_even(num):
            return True
        else:
            if is_sum_of_4_even(num - 2) or is_sum_of_4_even(num - 4) or is_sum_of_4_even(num - 6) or is_sum_of_4_even(num - 8):
                return True
            else:
                return False

        return False

    return is_sum_of_4_even(n)


# This code is contributed by Soumya Saurav

# Enter your code here. Read input from STDIN. Print output to STDOUT#

def check_sum_of_four_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    check_sum_of_four_even