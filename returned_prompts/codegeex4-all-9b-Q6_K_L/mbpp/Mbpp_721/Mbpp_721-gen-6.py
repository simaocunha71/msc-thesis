def maxAverageOfPath(grid: list) -> float:
  total_cost = 0
  num_cells = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      total_cost += grid[i][j]
      num_cells += 1
  return total_cost / num_cells

