
def is_equal_to_sum_even(n):
    # Write your code here
    for i in range(1, n+1):
        if i % 2 == 0:
            if n == i + i + i + i:
                return True
    return False
