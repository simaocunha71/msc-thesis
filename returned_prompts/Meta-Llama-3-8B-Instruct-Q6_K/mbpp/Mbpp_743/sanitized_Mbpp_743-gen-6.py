def rotate_right(lst, n):
  return lst[-n:] + lst[:-n] if n > 0 else lst[n:] + lst[:n] if n < 0 else lst