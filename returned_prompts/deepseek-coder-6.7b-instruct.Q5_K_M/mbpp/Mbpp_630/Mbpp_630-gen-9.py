
def get_coordinates(coordinate):
  x, y = coordinate
  result = []
  for i in range(-1, 2):
    for j in range(-1, 2):
      result.append([x+i, y+j])
  return result
"""
This function works by iterating over a range of -1 to 1 (inclusive) for both the x and y coordinates. For each pair of x and y values, it adds them to the result list as long as they are within the valid range for the grid.
"""

