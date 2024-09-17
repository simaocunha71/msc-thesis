
def odd_length_sum(arr):
  return sum(arr[i:j] for i in range(len(arr)) for j in range(i+1, len(arr)+1) if len(arr[i:j]) % 2 == 1)


