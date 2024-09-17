def is_Monotonic(mono_arr: list) -> bool:
  mono_flag = True
  for i in range(len(mono_arr)-1):
    if mono_arr[i] < mono_arr[i+1]:
      mono_flag = False
  return mono_flag