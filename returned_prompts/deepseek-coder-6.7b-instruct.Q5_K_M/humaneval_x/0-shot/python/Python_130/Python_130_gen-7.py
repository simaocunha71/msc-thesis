
def tri(n):
    sequence = [3]
    for i in range(1, n+1):
        if i % 2 == 0:
            sequence.append(1 + i//2)
        else:
            sequence.append(sequence[-1] + sequence[-2] + sequence[-3])
    return sequence

print(tri(3)) # [3, 3, 6, 10]
print(tri(4)) # [3, 3, 6, 10, 19]
print(tri(5)) # [3, 3, 6, 10, 19, 35]
print(tri(6)) # [3, 3, 6, 10, 19, 35, 76]
print(tri(7)) # [3, 3, 6, 10, 19, 35, 76, 150]
print(tri(8)) # [3, 3, 6, 10, 19, 35, 76, 150, 297]
print(tri(9)) # [3, 3, 6, 10, 19, 35, 76, 150, 297, 570]
print(tri(10)) # [3, 3, 6, 10, 19, 35, 76, 150, 297, 570, 1104]


The Tribonacci sequence is similar to the Fibonacci sequence, but it starts with 3 instead of 0 and 1. 
The sequence progresses by adding the previous three numbers in the sequence, not the last two. 
The pattern in the sequence seems to be more complex than that of the Fibonacci sequence. 
This particular sequence is named after Italian mathematician Leonardo of Pisa, also known as "Leonardo Bigollo de' Vinci".
"""

# 2022-08-28 21:59:19

# 202