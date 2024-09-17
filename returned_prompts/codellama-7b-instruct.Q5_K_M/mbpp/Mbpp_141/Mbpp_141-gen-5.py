
def pancake_sort(my_list):
  for i in range(len(my_list), 0, -1):
    if my_list[i-1] == i:
      continue
    my_list.reverse()
    my_list.pop()
    my_list.reverse()
    i -= 1
  return my_list


