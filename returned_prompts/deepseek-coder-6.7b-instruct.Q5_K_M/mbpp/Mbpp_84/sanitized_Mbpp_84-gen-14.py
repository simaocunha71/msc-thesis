def sequence(n):
  if n == 1 or n == 2:
    return 1
  else:
    sequence = [0, 1, 1]
    for i in range(3, n+1):
      sequence.append(sequence[sequence[i-1]] + sequence[i-sequence[i-2]])
    return sequence[n]