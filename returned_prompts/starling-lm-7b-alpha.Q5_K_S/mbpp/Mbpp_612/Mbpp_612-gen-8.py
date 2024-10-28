
def merge(sublists: list) -> list:
  firsts = [sublist[0] for sublist in sublists]
  seconds = [sublist[1] for sublist in sublists]
  return [firsts, seconds]


