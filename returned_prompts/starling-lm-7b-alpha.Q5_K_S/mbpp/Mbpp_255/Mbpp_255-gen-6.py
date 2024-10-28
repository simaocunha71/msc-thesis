
def combinations_colors(colors:list, n:int) -> list:
  return [tuple(color for _ in range(n)) for color in colors]


