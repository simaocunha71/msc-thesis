
def is_Monotonic(my_list: list) -> bool:
  if len(my_list) <= 1:
    return True
  is_inc = all(my_list[i] <= my_list[i+1] for i in range(len(my_list)-1))
  is_dec = all(my_list[i] >= my_list[i+1] for i in range(len(my_list)-1))
  return is_inc or is_dec


