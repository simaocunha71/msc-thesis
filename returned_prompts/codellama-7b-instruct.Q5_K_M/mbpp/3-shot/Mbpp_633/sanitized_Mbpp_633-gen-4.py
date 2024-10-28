def pair_xor_Sum(arr,n):
  return sum([a^b for a,b in zip(arr,arr[1:])])