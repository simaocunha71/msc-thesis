def next_smallest_palindrome(n: int) -> int:
  n_str = str(n)
  if n_str == n_str[::-1]:
    return int(n_str) + 1
  else:
    n_str = n_str[::-1]
    n_str = n_str[:-1] + str(int(n_str[-1]) + 1)
    return int(n_str[::-1])