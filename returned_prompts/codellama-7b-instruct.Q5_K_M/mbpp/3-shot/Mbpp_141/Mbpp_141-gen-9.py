
def pancake_sort(my_list):
  for i in range(len(my_list)-1,-1,-1):
    for j in range(i+1):
      if my_list[i] < my_list[j]:
        my_list[i], my_list[j] = my_list[j], my_list[i]
    my_list = my_list[0:i+1] + my_list[0:i] + my_list[i+1:]
  return my_list


