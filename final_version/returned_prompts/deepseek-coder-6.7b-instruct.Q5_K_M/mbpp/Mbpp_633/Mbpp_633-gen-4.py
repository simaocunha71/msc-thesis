def pair_xor_Sum(arr, n):
    sum = 0
    for i in range(0, 32):
        c = 0
        for j in range(0, n):
            if ((arr[j] & (1 << i))):
                c += 1
        sum += c * (n - c) * 2
    return sum

arr = [5, 9, 7, 6]
n = len(arr)
print(pair_xor_Sum(arr, n))

"""
In this python function, we are going through each bit of every number (from 0 to 31), and then for each bit, we are counting the numbers that have set bit at that position.

Then, using the formula for xor of all pairs, we are calculating the sum of xor of all pairs.
"""

# Time Complexity: O(n*32)
# Space Complexity: O(1)
<jupyter_output>
47
<jupyter_text>
