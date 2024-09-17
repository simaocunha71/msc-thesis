
def pack_consecutive_duplicates(my_list):
  result = []
  for i in range(len(my_list)):
    if i == 0:
      temp = [my_list[i]]
    else:
      if my_list[i] == my_list[i-1]:
        temp.append(my_list[i])
      else:
        result.append(temp)
        temp = [my_list[i]]
    if i == len(my_list) - 1:
      result.append(temp)
  return result


