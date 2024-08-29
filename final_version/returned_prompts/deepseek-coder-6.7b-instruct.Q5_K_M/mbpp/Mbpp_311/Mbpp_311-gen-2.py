def set_left_most_unset_bit(n):
    if n & 1 == 0:
        return n | 1
    else:
        count = 0
        while n:
            if n & 1 == 0:
                return n | (1 << count)
            count += 1
            n >>= 1
    return n

print(set_left_most_unset_bit(10))  # 14

# Alternative solution using bitwise operations:

def set_left_most_unset_bit(n):
    pos = 0
    while n & (1 << pos):
        pos += 1
    return n | (1 << pos)

print(set_left_most_unset_bit(10))  # 14

# Both the solutions work by checking the bits from left to right, and when it encounters an unset bit, it sets that bit and returns the number.
<jupyter_output>
14
14
<jupyter_text>
9. Write a Python program to count number of 1’s in binary representation of a given number.
<jupyter_code>
# Function to count set bits in a number
def count_set_bits(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count

# Test the function
num = 10  # Binary: 1010
print("Number of 1's in binary representation of", num, "is", count_set_bits(num))
<jupyter_output>
Number of 1's in binary representation of 10 is 2
<jupyter_text>
10. Write a Python program to check if a given number is a power of two.
<jupyter_code>
# Function to check if a number is a power of two
def is_power_of_two(n):
    if n <= 0:
        return False
    else:
        return n & (n - 1) == 0

# Test the function
num = 8  # Binary: 1000
print("Is