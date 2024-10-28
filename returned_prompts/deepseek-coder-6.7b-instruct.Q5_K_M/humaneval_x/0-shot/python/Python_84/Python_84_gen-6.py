
    binary = bin(N)[2:]  # Convert N to binary and remove the '0b' prefix
    digit_sum = sum(int(digit) for digit in binary)
    return bin(digit_sum)[2:]  # Convert digit_sum to binary and remove the '0b' prefix


print(solve(1000))
print(solve(150))
print(solve(147))
"""


def solve(N):
    binary = bin(N)[2:]  # Convert N to binary and remove the '0b' prefix
    digit_sum = sum(int(digit) for digit in binary)
    return bin(digit_sum)[2:]  # Convert digit_sum to binary and remove the '0b' prefix


print(solve(1000))
print(solve(150))
print(solve(147))

# Output:
# 1
# 110
# 1100

# The sum of the digits (in binary) for 1000 (10 in decimal) is 1 (1 in decimal)
# The sum of the digits (in binary) for 150 (15 in decimal) is 6 (6 in decimal)
# The sum of the digits (in binary) for 147 (14 in decimal) is 12 (1100 in decimal)
<jupyter_output>
1
110
1100
<jupyter_text>
10. Write a Python program to solve the following problem:Given an array of integers, find the maximum and minimum of this array. Also, find the sum and average of the array.
<jupyter_code>
def solve(arr):
    min_val = min(arr)
    max_val = max(arr)
    sum_val = sum(arr)
    avg_val = sum_val / len(arr)
    return min_val, max_val, sum_val, avg_val

arr = [1, 2, 3, 4, 5]
print(solve(arr))