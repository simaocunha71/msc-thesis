def get_max_sum(n:int):
  if n == 0:
    return 0
  if n in (1,2,3,4,5):
    return n
  if n%2 == 0 or n%3 == 0 or n%4 == 0 or n%5 == 0:
    return max(n, get_max_sum(n//2) + get_max_sum(n//3) + get_max_sum(n//4) + get_max_sum(n//5))
  else:
    return get_max_sum(n-1) + get_max_sum(n-2) + get_max_sum(n-3) + get_max_sum(n-4) + get_max_sum(n-5)