
def check_occurences(my_list: list) -> dict:
  unique_tuples = {}
  for i in my_list:
    if i in unique_tuples:
      unique_tuples[i] += 1
    else:
      unique_tuples[i] = 1
  return unique_tuples


