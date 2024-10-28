def validate(num: int) -> bool:
  num_str = str(num)
  num_dict = {}
  for i in num_str:
    if i not in num_dict:
      num_dict[i] = 1
    else:
      num_dict[i] += 1
  for i in num_dict:
    if num_dict[i] > int(i):
      return False
  return True