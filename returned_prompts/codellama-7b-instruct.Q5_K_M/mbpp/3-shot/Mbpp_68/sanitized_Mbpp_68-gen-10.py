def is_Monotonic(my_list: list) -> bool:
  return all(my_list[i] <= my_list[i + 1] for i in range(len(my_list) - 1))