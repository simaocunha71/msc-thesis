def rotate_right(lst, n):
  n = n % len(lst)
  return lst[-n:] + lst[:-n]  # or lst[n:] + lst[:n] for left rotation