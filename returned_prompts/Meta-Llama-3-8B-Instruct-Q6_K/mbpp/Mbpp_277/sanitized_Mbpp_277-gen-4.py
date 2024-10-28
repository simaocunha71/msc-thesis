def dict_filter(d, n):
  return {key: value for key, value in d.items() if value >= n}  # filter dictionary with values greater than or equal to n