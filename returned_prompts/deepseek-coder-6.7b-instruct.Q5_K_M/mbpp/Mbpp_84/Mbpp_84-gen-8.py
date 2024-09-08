def sequence(n):
    if n == 1 or n == 2:
        return 1
    seq = [0, 1, 1]
    for i in range(3, n + 1):
        seq.append(seq[seq[i - 1]] + seq[i - seq[i - 2]])
    return seq[n]

print(sequence(10))
<jupyter_output>
6
<jupyter_text>
2. Write a function that will take a string as an input and reverse the string without using any built-in Python functions to reverse the string.
<jupyter_code>
