def count_occurance(main_string:str, sub_string:str) -> int:
  count = 0
  for i in range(len(main_string)):
    if main_string[i:i+len(sub_string)] == sub_string:
      count += 1
  return count