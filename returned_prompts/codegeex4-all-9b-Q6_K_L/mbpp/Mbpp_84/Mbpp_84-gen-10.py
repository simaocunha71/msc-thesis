def sequence(n):
  if n==1 or n==2:
    return 1
  sequence_list = [1,1]
  for i in range(2,n):
    sequence_list.append(sequence_list[i-1]+sequence_list[i-2])
  return sequence_list[n-1]