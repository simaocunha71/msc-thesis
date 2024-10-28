def pair_wise(lst: list) -> list:
  result = [(lst[i], lst[i+1]) for i in range(len(lst)-1)]
  return result