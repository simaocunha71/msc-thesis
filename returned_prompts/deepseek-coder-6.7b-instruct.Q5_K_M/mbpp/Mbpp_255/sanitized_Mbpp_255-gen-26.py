from itertools import combinations_with_replacement as cwr
def combinations_colors(color_list, n):
  return [x for x in cwr(color_list, n)]