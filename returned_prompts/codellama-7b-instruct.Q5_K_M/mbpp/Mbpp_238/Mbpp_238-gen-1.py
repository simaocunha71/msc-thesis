
def number_of_substrings(input_str: str) -> int:
  count = 0
  for i in range(len(input_str)):
    for j in range(i,len(input_str)):
      if input_str[i] != input_str[j] and input_str[i] != "" and input_str[j] != "":
        count += 1
  return count


