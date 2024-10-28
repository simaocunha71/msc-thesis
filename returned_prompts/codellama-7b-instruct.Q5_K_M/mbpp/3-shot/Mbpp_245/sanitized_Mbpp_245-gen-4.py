def max_sum(arr: list) -> int:
  if len(arr) == 1:
    return arr[0]
  elif len(arr) == 2:
    return max(arr[0], arr[1])
  else:
    m1 = max(arr[:len(arr)//2])
    m2 = max(arr[len(arr)//2:])
    return max(m1 + max_sum(arr[len(arr)//2:]), m2 + max_sum(arr[:len(arr)//2]))