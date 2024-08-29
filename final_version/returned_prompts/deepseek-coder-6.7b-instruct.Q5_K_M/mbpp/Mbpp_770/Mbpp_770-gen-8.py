def odd_num_sum(n):
    sum = 0
    for i in range(1, 2*n, 2):
        sum += i**4
    return sum

# Testing
assert odd_num_sum(2) == 82

# The function works by initializing a sum variable to 0. Then it loops from 1 through 2n with a step of 2 (i.e., only odd numbers). For each number, it takes the fourth power (i**4) and adds it to the sum. Finally, it returns the sum.
<jupyter_output>
<empty_output>
<jupyter_text>
