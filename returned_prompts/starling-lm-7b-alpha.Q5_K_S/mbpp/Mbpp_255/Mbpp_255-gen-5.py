
def combinations_colors(colors:list, length:int) -> list:
  return [tuple(color) for color in powerset(colors, length)]

def powerset(s,k):
  if k==0:
    return [()]
  else:
    return [x+y for x in powerset(s,k-1) for y in s if y not in x]


