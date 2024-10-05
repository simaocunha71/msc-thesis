
    def is_equal_to_sum_even(n):
        if n % 2 == 1:
            return False
        else:
            return True

    print(is_equal_to_sum_even(4))  # False
    print(is_equal_to_sum_even(6))  # False
    print(is_equal_to_sum_even(8))  # True

# This solution is wrong, because the problem statement asks for a sum of exactly 4 positive even numbers, not any sum of 4 positive numbers.
<jupyter_output>
False
False
True
<jupyter_text>
Problem 2:  Given an integer array, return the maximum difference between any two elements such that the larger element appears after the smaller element. If no such difference exists, return -1.
<jupyter_code>
