def newman_conway(n):
    sequence = [0, 1, 1]
    for i in range(3, n+1):
        sequence.append(sequence[sequence[i-1]] + sequence[i-sequence[i-1]])
    return sequence[n]

print(newman_conway(10))

# Q2
