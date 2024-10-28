
def pancake_sort(my_list):
  for i in range(len(my_list)):
    for j in range(i, len(my_list)):
      if my_list[j] < my_list[i]:
        my_list[i], my_list[j] = my_list[j], my_list[i]
    my_list.reverse()
  return my_list


