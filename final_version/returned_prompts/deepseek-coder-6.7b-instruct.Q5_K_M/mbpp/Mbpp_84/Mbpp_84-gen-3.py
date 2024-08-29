def newman_conway(n):
    sequence = [0, 1, 1]
    for i in range(3, n+1):
        sequence.append(sequence[sequence[i-1]] + sequence[i-sequence[i-1]])
    return sequence[n]

print(newman_conway(10))  # Output: 6

Explanation:
The Newman-Conway sequence is a sequence of numbers that starts with three terms, 1, 1, and 1. After that, each number is the sum of the two previous numbers. However, if a number has been seen before, it's replaced with the number of steps taken to reach this number. For example, the 7th term of the sequence is 4 because we have seen 1 before (step 1), the 8th term is 5 because we have seen 2 before (step 2), the 9th term is 6 because we have seen 3 before (step 3), and the 10th term is 6 because we have seen 4 before (step 4).
"""

