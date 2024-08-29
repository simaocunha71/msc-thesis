def odd_Equivalent(bin_str, rotations):
    n = len(bin_str)
    bin_str = bin_str + bin_str
    rotated_bin_str = [bin_str[i:i+n] for i in range(n)]
    for i in range(rotations):
        rotated_bin_str.append(rotated_bin_str.pop(0))
    odd_count = 0
    for bin_str in rotated_bin_str:
        if int(bin_str,2) % 2 != 0:
            odd_count += 1
    return odd_count

# test cases to validate the solution
assert odd_Equivalent("011001",6) == 3
assert odd_Equivalent("000000",6) == 6
assert odd_Equivalent("111111",6) == 6
assert odd_Equivalent("101010",6) == 0
assert odd_Equivalent("110011",6) == 4
<jupyter_output>
<empty_output>
<jupyter_text>
Q2:Find the total number of ways to partition a set into two subsets such that the sum of elements in both subsets is the same.
<jupyter_code>
