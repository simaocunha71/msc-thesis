def sequence(n):
  if n in [1, 2]:
    return 1
  sequence_list = [1, 1]
  while len(sequence_list) < n:
    sequence_list.append(sequence_list[-1] + sequence_list[-2])
  return sequence_list[-1]