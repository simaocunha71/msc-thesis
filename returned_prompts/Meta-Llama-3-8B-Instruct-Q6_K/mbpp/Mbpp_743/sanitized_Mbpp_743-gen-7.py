def rotate_right(lst, n):
  n = n % len(lst)
  return lst[-n:] + lst[:-n]  # Python slice syntax: lst[-n:] for last n elements and lst[:-n] for all but last n elements