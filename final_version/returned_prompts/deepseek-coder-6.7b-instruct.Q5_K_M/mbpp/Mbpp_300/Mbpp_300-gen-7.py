
def count_binary_seq(n):
    # Total number of binary sequences of length 2n is 2^2n.
    total_seq = 2 ** (2 * n)
    
    # For the sum of first n bits to be equal to sum of last n bits, we have 2^n choices for each bit.
    # So, number of such sequences is (2^n)^2.
    equal_sum_seq = (2 ** n) ** 2
    
    # Total number of sequences where sum of first n bits is not equal to sum of last n bits is total_seq - equal_sum_seq.
    not_equal_sum_seq = total_seq - equal_sum_seq
    
    return equal_sum_seq, not_equal_sum_seq

print(count_binary_seq(1))  # Expected output: (4, 2)

# The first element in the tuple returned by the function is the count of binary sequences where the sum of the first n bits is equal to the sum of the last n bits.
# The second element in the tuple returned by the function is the count of binary sequences where the sum of the first n bits is not equal to the sum of the last n bits.

# The function works by first calculating the total number of binary sequences of length 2n.
# It then calculates the number of sequences where the sum of the first n bits is equal to the sum of the last n bits.
# The number of sequences where the sum of the first n bits is not equal to the sum of the last n bits is then calculated by subtracting the count of sequences where the sum is equal from the total count.
<jupyter_output>
(4, 2)
<jupyter_text>
Question 2
<jupyter_code>
