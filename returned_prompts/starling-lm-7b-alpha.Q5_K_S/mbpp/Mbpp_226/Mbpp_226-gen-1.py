
def odd_values_string(s: str) -> str:
  odd_index = [i for i in range(len(s)) if (i+1) % 2 == 1]
  odd_index_length = len(odd_index)
  odd_index_list = s[odd_index[0]:odd_index[odd_index_length-1]+1]
  return odd_index_list


