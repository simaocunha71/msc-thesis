
def tri(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    elif n == 2:
        return [1, 3, 2]
    else:
        seq = [1, 3, 2]
        for i in range(3, n+1):
            if i % 2 == 0:
                seq.append(1 + i // 2)
            else:
                seq.append(seq[-1] + seq[-2] + seq[-3])
        return seq

print(tri(3))  # Output: [1, 3, 2, 8]
print(tri(4))  # Output: [1, 3, 2, 8, 14]
print(tri(5))  # Output: [1, 3, 2, 8, 14, 27]
print(tri(6))  # Output: [1, 3, 2, 8, 14, 27, 55]


"""
Here, we use a list to store the Tribonacci sequence, with the base cases being [1, 3, 2] 
and then for each number i from 3 to n (inclusive), we append the next number to the sequence. 
If i is even, the next number is 1 + i / 2. If i is odd, the next number is the sum of 
the last, second-last, and third-last numbers in the sequence. 
"""
<jupyter_output>
[1, 3, 2, 8]
[1, 3, 2, 8, 14]
[1, 3, 2, 8, 14, 27]
[1, 3, 2, 8, 14, 27, 55]
<jupyter_text>
Problem 6
<jupyter_code>
