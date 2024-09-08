"""
Here is the python code for the problem:

def newman_conway(n):
    if n == 1:
        return '1'
    if n == 2:
        return '1 1'
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[seq[i-1]] + seq[i-seq[i-1]])
    return ' '.join(map(str, seq))

print(newman_conway(10))

This will return the sequence up to the nth number.
"""


# Problem 2
