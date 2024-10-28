
def max_run_uppercase(string):
  upper_list = []
  for i in range(len(string)):
    if string[i].isupper():
      if i == 0 or string[i-1].islower():
        upper_list.append(string[i])
    else:
      if len(upper_list) > 0:
        break
  return len(upper_list)


