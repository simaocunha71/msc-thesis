def next_power_of_2(n: int) -> int:
    if n <= 0:
        return 1
    else:
        return 2 ** (n - 1).bit_length()


print(next_power_of_2(0))  # 1

# bit_length() method returns the number of bits required to represent an integer in binary format.
# For example, bin(12).bit_length() returns 4.
# Therefore, (n - 1).bit_length() returns the smallest power of 2 that is not less than n.
# We then return 2 raised to this power.

#bit_length() method will give the correct power of 2 that is greater than or equal to n,
# but it will also return 0 for n=0, so we return 1 in that case.
<jupyter_output>
1
<jupyter_text>
Task 2
<jupyter_code>
