
def comb_sort(my_list):
  gap = len(my_list)
  swapped = True
  while swapped:
    gap = int(gap/1.25)
    if gap < 1:
      gap = 1
      swapped = False
    for i in range(len(my_list)-gap):
      if my_list[i] < my_list[i+gap]:
        my_list[i], my_list[i+gap] = my_list[i+gap], my_list[i]
        swapped = True
  return my_list

