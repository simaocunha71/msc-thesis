
def count_occurance(given_str:str) -> int:
  count = 0
  for i in range(len(given_str)):
    if given_str[i:i+3] == 'std':
      count += 1
  return count


